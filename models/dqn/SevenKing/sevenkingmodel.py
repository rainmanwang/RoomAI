import dqn
import roomai
import roomai.sevenking
import tensorflow as tf

class SevenKingModel(dqn.DQNModel):
    def __init__(self, model_address = None, params = dict()):
        self.num_point  = 15
        self.num_suit   = 4
        self.info_dim   = 4
        self.action_dim = 4

        self.learning_rate = 0.001
        if "learning_rate" in params:
            self.learning_rate = params["learning_rate"]

        self.weight_decay = 0.004
        if "weight_decay" in params:
            self.weight_decay = params["weight_decay"]

        self.print_step = 200
        if "print_step" in params:
            self.print_step = params["print_step"]

        self.model_address = model_address
        self.graph         = tf.Graph()

        with self.graph.as_default() as graph:
            self.info_feat   = tf.placeholder(tf.float32, [None, self.num_point, self.num_suit, self.info_dim])
            self.action_feat = tf.placeholder(tf.float32, [None, self.num_point, self.num_suit, self.action_dim])


    def _variable_on_cpu(name, shape, initializer):
        """Helper to create a Variable stored on CPU memory.
        Args:
        name: name of the variable
        shape: list of ints
        initializer: initializer for Variable
        Returns:
        Variable Tensor
        """
        with tf.device('/cpu:0'):
            dtype = tf.float32
            var = tf.get_variable(name, shape, initializer=initializer, dtype=dtype)
        return var

    def _variable_with_weight_decay(name, shape, stddev, wd):
        """Helper to create an initialized Variable with weight decay.
          Note that the Variable is initialized with a truncated normal distribution.
        A weight decay is added only if one is specified.
        Args:
            name: name of the variable
            shape: list of ints
            stddev: standard deviation of a truncated Gaussian
            wd: add L2Loss weight decay multiplied by this float. If None, weight
            decay is not added for this Variable.
        Returns:
         Variable Tensor
        """
        dtype = tf.float32
        var = _variable_on_cpu(
            name,
            shape,
            tf.truncated_normal_initializer(stddev=stddev, dtype=dtype))
        if wd is not None:
            weight_decay = tf.multiply(tf.nn.l2_loss(var), wd, name='weight_loss')
            tf.add_to_collection('losses', weight_decay)
        return var

    def gen_action_feat(self, action):
        pass
    def gen_info_feat(self, info):
        pass
    def terminal_info_feat(self):
        pass
    def terminal_action_feat(self):
        pass
    def take_action(self, info):
        pass
    def update_model(self, experiences):
        pass

if __name__ == "__main__":
    env   = roomai.sevenking.SevenKingEnv()
    model = SevenKingModel()
    dqn   = dqn.DQN()
    dqn.train(env=env,model=model)