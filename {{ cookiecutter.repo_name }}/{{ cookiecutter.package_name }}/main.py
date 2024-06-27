# python class to run everything


class DataTransformer:
    # ETL helper class
    def __init__(self, data_path):
        self.data_path = data_path


class DataScienceHelper:
    def __init__(self, data_path, experiment_name) -> None:
        self.data_path = data_path
        self.experiment_name = experiment_name

    def run_experiment(self, model_params):
        # model_params should be a dict i.e. model_params['model_type']

        # Insert pipeline stuff here
        pass


if __name__ == "__main__":
    pass
