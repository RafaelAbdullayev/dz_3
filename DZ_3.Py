class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def info(self):
        return f"{self.last_name} {self.first_name}, {self.age} лет"


class Student(Human):
    def __init__(self, first_name, last_name, age, major, group, avg_score):
        super().__init__(first_name, last_name, age)
        self.major = major
        self.group = group
        self.avg_score = avg_score

    def info(self):
        base = super().info()
        return f"{base} — Студент: {self.major}, группа {self.group}, ср. балл: {self.avg_score}"


class Graduate(Student):
    def __init__(self, first_name, last_name, age, major, group, avg_score, diploma_topic):
        super().__init__(first_name, last_name, age, major, group, avg_score)
        self.diploma_topic = diploma_topic

    def info(self):
        base = super().info()
        return f"{base}, диплом: «{self.diploma_topic}»"


class Teacher(Human):
    def __init__(self, first_name, last_name, age, subject, skill_level):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.skill_level = skill_level

    def info(self):
        base = super().info()
        return f"{base} — Преподаватель по предмету: {self.subject}, уровень: {self.skill_level}"


# Примеры объектов
group = [
    Student("Даши", "Батодалаев", 16, "ГК", "Web_011", 5),
    Student("Линар", "Загидуллин", 32, "РПО", "PD_011", 5),
    Graduate("Сергей", "Шугаин", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
    Teacher("Андрей", "Даншин", 38, "Астрофизика", 110),
    Student("Даниил", "Маркин", 17, "ГК", "Python_011", 5),
    Teacher("Алексей", "Башкиров", 45, "Разработка приложений", 20)
]

# Вывод информации
for person in group:
    print(person.info())
