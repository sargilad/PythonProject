import csv
import os.path
from operator import itemgetter


class HighScoreManager:
    __high_score_file = ""

    def __init__(self, high_score_file):
        self.__high_score_file = high_score_file

    def read_file(self):
        rows = []
        if os.path.isfile(self.__high_score_file):
            with open(self.__high_score_file, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    # print(row['id'], row['name'], row['country'])
                    dict = {row['name']: row['score']}
                    rows.append(dict)
        return rows

    def write_file(self, data):
        with open(self.__high_score_file, 'w', newline='') as csvfile:
            fieldnames = ['name', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for entity in data:
                # writer.writerow({'id': '10', 'name': 'moshe', 'country': 'israel'})
                # writer.writerow({'id': '20', 'name': 'david', 'country': 'england'})
                writer.writerow(entity)

    def append_file(self, data):
        with open(self.__high_score_file, 'a', newline='') as csvfile:
            fieldnames = ['name', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(data)

    def is_new_high_score(self, score: int) -> bool:
        high_scores = self.read_file()
        for high_score in range(len(high_scores)):
            for key in high_scores[high_score]:
                if score > int(high_scores[high_score][key]):
                    return True

        return False

    def add_high_score_to_file(self, high_score_dict):
        high_scores = self.read_file()
        if len(high_scores) < 3:
            self.append_file(high_score_dict)
        else:
            if self.is_new_high_score(high_score_dict['score']):
                high_scores.append({high_score_dict['name']:high_score_dict['score']})
                self.__filter_highest_scores(high_scores, 3)


    def __filter_highest_scores(self, high_scores:list , count):
        # high_scores= sorted(high_scores, key=itemgetter('score'))
        high_scores.sort(key=lambda k: k['score'])
        print()
