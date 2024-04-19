from enum import Enum, auto


class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, city_code: str):
        seasons = {
            self.WINTER.name: ["winter", "зима"],
            self.SPRING.name: ["spring", "весна"],
            self.SUMMER.name: ["summer", "лето"],
            self.FALL.name: ["fall", "осень"],
        }
        if city_code == "en":
            return seasons[self.name][0]
        if city_code == "ru":
            return seasons[self.name][1]


    #    seasons_translate = {
    #         'en': {
    #             self.WINTER: 'winter',
    #             self.SPRING: 'spring',
    #             self.SUMMER: 'summer',
    #             self.FALL: 'fall'
    #         },
    #         'ru': {
    #             self.WINTER: 'зима',
    #             self.SPRING: 'весна',
    #             self.SUMMER: 'лето',
    #             self.FALL: 'осень'
    #         },
    #     }
    #     return seasons_translate[country_code][self]

# INPUT DATA:

# TEST_1:
print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))

# TEST_2:
for season in Seasons:
    print(season.text_value('en'), '->', season.text_value('ru'))

# TEST_3:
for season in Seasons:
    print(season.name, season.value)