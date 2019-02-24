from keras.optimizers import Adam


class Config(dict):
    def __getattr__(self, name):
        if name[0] == "_":
            raise AttributeError(name)
        return self[name]

    """
    def __repr__(self):
        return f"Config({', '.join(k + '=' + repr(v) for k,v in self.items())})"
    """

    def __add__(self, other):
        return Config(**{**self, **other})


train_config = Config(episodes=100, time_limit=500)
nn_config = Config(loss="mse", optimizer=Adam(lr=0.001))
memory_config = Config(batch_size=32, size=1000)
policy_config = Config(e=0.2, e_decay=0.995, e_min=0.0001)
update_config = Config(gamma=0.999)