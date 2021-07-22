#/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import datasets, linear_model

class Traintest:

    def __init__(self,train, test, output):
        self.train = train
        self.test = test
        self.output = output

    def trainer(self):
        try:
            data = pd.read_csv(self.train)
        except Exception as exc:
            print("Could not read the file")
        array = data.values

        for i in range(len(array)):
            if array[i][1] == "Male":
                array[i][1] = 1
            else:
                array[i][1] = 0

        df = pd.DataFrame(array)
        maindf = df[[1,2,3,4,5,6,7,8,9]]
        mainarray = maindf.values
        tempdf = df[10]

        train_y = tempdf.values
        for i in range(len(train_y)):
            train_y[i] = str(train_y[i])
        self.learn = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter=13000)
        self.learn.fit(mainarray, train_y)
        print(self.learn.fit(mainarray, train_y))

    def testing(self):
        try:
            self.testdata = pd.read_csv(self.test)
        except ParserError:
            print("Could not read the file")
        tester_array = self.testdata.values

        for i in range(len(tester_array)):
            if tester_array[i][1] == "Male":
                tester_array[i][1] = 1
            else:
                tester_array[i][1] = 0

        dft = pd.DataFrame(tester_array)
        testdf = dft[[1,2,3,4,5,6,7,8,9]]
        maintestarray = testdf.values
        self.x_predict = self.learn.predict(maintestarray)
        for i in range(len(self.x_predict)):
            self.x_predict[i] = str(self.x_predict[i])
        #runs successfully

    def back_to_df(self):
        self.bdf = pd.DataFrame(self.x_predict, columns=['Predicted Career'])
        self.bdf.index = self.bdf.index
        self.bdf.to_csv('predicted_careers_only_system.csv', index=False)
    def combine_data(self):
        main = pd.read_csv(self.test)
        dataframe = pd.DataFrame(main)
        dataframe2 = self.bdf
        concat = pd.concat([dataframe,dataframe2], axis=1).reindex(dataframe.index)
        concat.to_csv(self.output, index=False)
        print("\033[92m Done successfully")

"""
class OnePerson(Traintest):

    def __init__(self, data: list or tuple):
        self.data = data

    def check_data(self):
        if type(self.data[1]==str):
                continue
        elif data[1] is not "Male" or "Female":
            print("Gender is Male of Female")
        else:
            print("Subjects must be integers ranginging from 1 to 12")

    def testing(self):
        if data[1] == "Male":
            data[1] = 1
        else data[1] = 0
        array = np.array(self.data)
        df = pd.DataFrame(array)
        testdf = df[[0,1,2,3,4,5,6,7,8,9]]
        maintestarray = testdf.values
        x_predict = self.learn.predict(maintestarray)
        return x_predict
"""
