import codecs
import collections
import numpy as np
import tensorflow as tf

# 定义LSTM模型
def neural_network(model='lstm', rnn_size=128, num_layers=2):
    if model == 'rnn':
        cell_fun = tf.nn.rnn_cell.BasicRNNCell
    elif model == 'gru':
        cell_fun = tf.nn.rnn_cell.GRUCell
    elif model == 'lstm':
        cell_fun = tf.nn.rnn_cell.BasicLSTMCell

    cell = cell_fun(rnn_size, state_is_tuple=True)
    cell = tf.nn.rnn_cell.MultiRNNCell([cell] * num_layers, state_is_tuple=True)

    initial_state = cell.zero_state(1, tf.float32)

    with tf.variable_scope('rnnlm'):
        softmax_w = tf.get_variable("softmax_w", [rnn_size, len(words)])
        softmax_b = tf.get_variable("softmax_b", [len(words)])
        with tf.device("/cpu:0"):
            embedding = tf.get_variable("embedding", [len(words), rnn_size])
            inputs = tf.nn.embedding_lookup(embedding, input_data)

    outputs, last_state = tf.nn.dynamic_rnn(cell, inputs, initial_state=initial_state, scope='rnnlm')
    output = tf.reshape(outputs, [-1, rnn_size])

    logits = tf.matmul(output, softmax_w) + softmax_b
    probs = tf.nn.softmax(logits)
    return logits, last_state, probs, cell, initial_state


def to_word(weights):
    t = np.cumsum(weights)
    s = np.sum(weights)
    sample = int(np.searchsorted(t, np.random.rand(1) * s))
    return words[sample]


if __name__ == "__main__":
    poetry_file = './poetry_data/training_poetry.txt'

    # 数据预处理
    poetrys = []
    with codecs.open(poetry_file, "r", "utf-8") as f:
        for line in f:
            try:
                line = line.strip('\n')
                title, content = line.strip(' ').split(':')
                content = content.replace(' ', '')
                if '_' in content or '(' in content or '（' in content or '《' in content or '[' in content:
                    continue
                if len(content) < 5 or len(content) > 79:
                    continue
                content = '[' + content + ']'
                poetrys.append(content)
            except:
                pass

    # 按诗的字数排序
    poetrys = sorted(poetrys, key=lambda line: len(line))
    print('唐诗总数: ', len(poetrys))

    # 统计每个字出现次数
    all_words = []
    for poetry in poetrys:
        all_words += [word for word in poetry]
    counter = collections.Counter(all_words)
    count_pairs = sorted(counter.items(), key=lambda x: -x[1])
    words, _ = zip(*count_pairs)

    words = words[:len(words)] + (' ',)  # 取前多少个常用字
    word_num_map = dict(zip(words, range(len(words))))  # 每个字映射为一个数字ID

    input_data = tf.placeholder(tf.int32, [1, None])
    output_targets = tf.placeholder(tf.int32, [1, None])

    _, last_state, probs, cell, initial_state = neural_network()
    Session_config = tf.ConfigProto(allow_soft_placement=True)
    Session_config.gpu_options.allow_growth = True

    with tf.Session(config=Session_config) as sess:
        with tf.device('/gpu:0'):
            sess.run(tf.global_variables_initializer())

            saver = tf.train.Saver(tf.global_variables())
            latest_ckpt = tf.train.latest_checkpoint('poetry_model/')
            saver.restore(sess, latest_ckpt)

            state_ = sess.run(cell.zero_state(1, tf.float32))

            poem = "春"
            last_char = poem

            #times = 0
            while len(poem) < 24:
                x = np.zeros((1, 1))
                x[0, 0] = word_num_map[last_char]
                [probs_, state_] = sess.run([probs, last_state], feed_dict={input_data: x, initial_state: state_})
                word = to_word(probs_)

                if word != "，" and word != "]" and word != " " and word != "," and word != "。":
                    last_char = word
                    poem += word

                if len(poem) == 5 or len(poem) == 11 or len(poem) == 17:
                    poem += ","
                elif len(poem) == 23:
                    poem += "。"

            print(poem)
