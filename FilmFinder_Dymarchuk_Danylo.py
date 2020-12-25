import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_film_data():
    imdbdata = pd.read_csv('IMDB-Movie-Data.csv')
    imdbdata = imdbdata.rename(columns={'Revenue (Millions)': 'Revenue_Millions',
                                        'Runtime (Minutes)': 'Runtime_Minutes'})
    return imdbdata


def gerne_analysis(imdbdata):
    imdbdata["Genre"].value_counts()
    print("Ви знаходитесь в меню пошуку по жанрах.")
    seperate_genre = 'Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Fantasy, Family, \n' \
                     'History, Horror, Music, Musical, Mystery, Romance, Sci-Fi, Sport, Thriller, War, Western'
    print("У базі присутні фільми наступних жанрів:")
    print(seperate_genre)
    print()
    genre = input("Введіть жанр для якого буде визначено ТОП 5 найрейтинговіших фільмів:\t")

    if not genre in seperate_genre:
        print("Такого жанру у базі немає.")
        return


    df = imdbdata['Genre'].str.contains(genre).fillna(False)
    print('The total number of movies with ', genre, '=', len(imdbdata[df]))
    f, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Year', data=imdbdata[df], palette="Greens_d");
    plt.title(genre)
    plt.show()


def director_analysis(imdbdata):
    imdbdata.Director.value_counts()[:10].plot.pie(autopct='%1.1f%%', figsize=(10, 10))
    plt.title('TOP 10 DIRECTORS OF MOVIES')
    plt.show()


def actor_analysis(imdbdata):
    imdbdata.Actors.value_counts()[:10].plot.pie(autopct='%1.1f%%', figsize=(10, 10))
    plt.title('TOP 10 ActorS OF MOVIES')
    plt.show()


def year_analysis(imdbdata):
    imdbdata["Year"].value_counts()
    sns.stripplot(x="Year", y="Rating", data=imdbdata, jitter=True);
    plt.show()

    sns.swarmplot(x="Year", y="Votes", data=imdbdata);
    plt.show()

    sns.stripplot(x="Year", y="Revenue_Millions", data=imdbdata, jitter=True);
    plt.show()

    sns.swarmplot(x="Year", y="Metascore", data=imdbdata);
    plt.show()


def runtime_analysis(imdbdata):
    imdbdata["Runtime_Minutes"].value_counts()

    imdbdata.Runtime_Minutes.value_counts()[:10].plot.pie(autopct='%1.1f%%', figsize=(10, 10))
    plt.title('TOP 10 runtime OF MOVIES')
    plt.show()

    time = imdbdata.Runtime_Minutes
    sns.distplot(time, bins=20, kde=False, rug=True)
    plt.show()


def rating_analysis(imdbdata):
    imdbdata["Rating"].value_counts()
    print("top 10 rating movies")
    Sortedrating = imdbdata.sort_values(['Rating'], ascending=False)
    print(Sortedrating.head(10))

    print()

    print("low rated movies")
    lowratedmovies = imdbdata.query('(Rating > 0) & (Rating < 3.0)')
    print(lowratedmovies.head())

    print()

    print("medium rated movies")
    mediumratedmovies = imdbdata.query('(Rating > 3.0) & (Rating < 7.0)')
    print(mediumratedmovies.head())


def search_by_gerne(dataset):
    print("Ви знаходитесь в меню пошуку по жанрах.")
    seperate_genre = 'Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Fantasy, Family, \n' \
                     'History, Horror, Music, Musical, Mystery, Romance, Sci-Fi, Sport, Thriller, War, Western'
    print("У базі присутні фільми наступних жанрів:")
    print(seperate_genre)
    print()
    genre = input("Введіть жанр для якого буде визначено ТОП 5 найрейтинговіших фільмів:\t")

    if not genre in seperate_genre:
        print("Такого фанру у базі немає.")
        return
    print()
    print(dataset[dataset["Genre"].str.contains(genre)].sort_values(by="Rating", ascending=False)\
              [["Genre", "Title", "Rating"]].head(5))

def search_by_director(dataset):
    print("Ви знаходитесь в меню пошуку по режисеру.")
    director = input("Введіть прізвище або ім\'я режисера для якого буде визначено ТОП 5 найрейтинговіших фільмів:\t")

    print()
    print(dataset[dataset["Director"].str.contains(director)].sort_values(by="Rating", ascending=False)\
              [["Director", "Title", "Rating"]].head(5))


def search_by_actor(dataset):
    print("Ви знаходитесь в меню пошуку по акторах.")
    actor = input("Введіть прізвище або ім\'я актора для якого буде визначено ТОП 5 найрейтинговіших фільмів:\t")

    print()
    print(dataset[dataset["Actors"].str.contains(actor)].sort_values(by="Rating", ascending=False)\
              [["Actors", "Title", "Rating"]].head(5))


def search_by_year(dataset):
    print("Ви знаходитесь в меню пошуку по роках випуску.")
    print("Максимальна верхня межа = 2016")
    low = input("Введіть нижню межу пошуку по роках:\t")
    heigth = input("Введіть верхню межу пошуку по роках:\t")

    try:
        low = int(low)
        heigth = int(heigth)
    except:
        print("Ви ввели недопустиме значення!!!")
        return
    if low > heigth:
        print("Нижня межа повинна бути менша або рівна верхньої")
        return
    if heigth > 2016:
        print("Верхня межа повинна бути не більша 2016 року")
        return

    print()
    print(dataset[(dataset["Year"] >= low) & (dataset["Year"] <= heigth)].sort_values(by="Rating", ascending=False)\
              [["Year", "Title", "Rating"]].head(5))


def search_by_runtime(dataset):
    print("Ви знаходитесь в меню пошуку по тривалості фільму.")
    print("Максимальна верхня межа тривалості фільму 200 хв.")
    low = input("Введіть нижню межу тривалості у хвилинах:\t")
    heigth = input("Введіть верхню межу тривалості у хвилинах:\t")

    try:
        low = int(low)
        heigth = int(heigth)
    except:
        print("Ви ввели недопустиме значення!!!")
        return
    if low > heigth:
        print("Нижня межа повинна бути менша або рівна верхньої")
        return
    if heigth > 200:
        print("Верхня межа тривалості фільму повинна бути не більша 200 хв.")
        return

    print()
    print(dataset[(dataset["Runtime_Minutes"] >= low) & (dataset["Runtime_Minutes"] <= heigth)].\
          sort_values(by="Rating", ascending=False)\
              [["Runtime_Minutes", "Title", "Rating"]].head(5))


def search_by_rating(dataset):
    print()
    print(dataset.sort_values(by="Rating", ascending=False)[["Title", "Rating"]].head(5))


def count_of_books_by_genre():
    topics = pd.read_csv("DataSets/topics.csv")
    genre_count_tp = topics.groupby("Genre")["Genre"].count()
    genre_count_data_tp = pd.DataFrame({"Genre": genre_count_tp.index, "Count": genre_count_tp})
    print(genre_count_data_tp.sort_values(by="Count", ascending=False)["Count"].head())

def count_of_books_by_year():
    topics = pd.read_csv("DataSets/topics.csv")
    genre_count_tp_year = topics.groupby("Date of creation/publication")["Date of creation/publication"].count()
    genre_count_data_tp_year = pd.DataFrame({"Date of creation/publication": genre_count_tp_year.index, "Count": genre_count_tp_year})
    print(genre_count_data_tp_year.sort_values(by="Count", ascending=False)["Count"].head())
    print()


def main():
    while True:
        print()
        print("Оберіть варіант дій:")
        print("\t1. Аналіз даних")
        print("\t2. Пошук по критеріях")
        print("\t3. Пошук по книгах")
        print("\t4. Вихід")

        action = input("Введіть варіант дії:\t")
        print()
        try:
            act_case = int(action)
        except:
            print("Ви ввели недопустиме значення!!!")
            print("Спробуйте це раз")
            continue
        if act_case <=0 or act_case >= 5:
            print("Ви ввели неіснуючий варіант проведення аналізу.")
            print("Спробуйте це раз")
            continue
        if act_case == 4:
            print("Завершення роботи застосунку!!!")
            break

        if act_case == 1:
            while True:
                print()
                print("Ви знаходитесь в меню аналізу даних.")
                print("\tОберіть критерій по якому буде проведено аналіз даних:")
                print("\t\t1. Аналіз по жанрах")
                print("\t\t2. Аналіз по режисерах")
                print("\t\t3. Аналіз по акторах")
                print("\t\t4. Аналіз по роках випуску фільму")
                print("\t\t5. Аналіз по тривалості")
                print("\t\t6. Аналіз по рейтингу")
                print("\t\t7. Вихід з меню \"Аналіз даних\"")

                variant = input("Введіть варіант дії:\t")
                print()

                try:
                    var_case = int(variant)
                except:
                    print("Ви ввели недопустиме значення!!!")
                    print("Спробуйте це раз")
                    continue
                if var_case <= 0 or var_case >= 8:
                    print("Ви ввели неіснуючий варіант проведення аналізу.")
                    print("Спробуйте це раз")
                    continue
                if var_case == 7:
                    print("Вихід з меню \"Аналіз даних\"")
                    break
                try:
                    dataset = load_film_data()
                except:
                    print("Під час завантаження даних сталась помилка.")
                    print("Спробуйте це раз")
                    continue

                if var_case == 1:
                    gerne_analysis(dataset)
                if var_case == 2:
                    director_analysis(dataset)
                if var_case == 3:
                    actor_analysis(dataset)
                if var_case == 4:
                    year_analysis(dataset)
                if var_case == 5:
                    runtime_analysis(dataset)
                if var_case == 6:
                    rating_analysis(dataset)

        if act_case == 2:
            while True:
                print()
                print("Ви знаходитесь в меню пошуку по критеріях.")
                print("\tОберіть критерій по якому буде проведено пошук даних:")
                print("\t\t1. По жанру")
                print("\t\t2. По режисеру")
                print("\t\t3. По актору")
                print("\t\t4. По роках випуску фільму")
                print("\t\t5. По тривалості")
                print("\t\t6. По рейтингу")
                print("\t\t7. Вихід з меню \"Аналіз даних\"")

                variant = input("Введіть варіант дії:\t")
                print()

                try:
                    var_case = int(variant)
                except:
                    print("Ви ввели недопустиме значення!!!")
                    print("Спробуйте це раз")
                    continue
                if var_case <= 0 or var_case >= 8:
                    print("Ви ввели неіснуючий варіант проведення аналізу.")
                    print("Спробуйте це раз")
                    continue
                if var_case == 7:
                    print("Вихід з меню \"Пошук по критеріях\"")
                    break
                try:
                    dataset = load_film_data()
                except:
                    print("Під час завантаження даних сталась помилка.")
                    print("Спробуйте це раз")
                    continue

                if var_case == 1:
                    search_by_gerne(dataset)
                if var_case == 2:
                    search_by_director(dataset)
                if var_case == 3:
                    search_by_actor(dataset)
                if var_case == 4:
                    search_by_year(dataset)
                if var_case == 5:
                    search_by_runtime(dataset)
                if var_case == 6:
                    search_by_rating(dataset)

        if act_case == 3:
            while True:
                print()
                print("Ви знаходитесь в меню пошуку по книгах.")
                print("\tОберіть критерій по якому буде проведено пошук даних:")
                print("\t\t1. По підстрічці у жанру")
                print("\t\t2. По підстрічці у році")
                print("\t\t3. Вихід з меню \"Пошук по книгах\"")

                variant = input("Введіть варіант дії:\t")
                print()

                try:
                    var_case = int(variant)
                except:
                    print("Ви ввели недопустиме значення!!!")
                    print("Спробуйте це раз")
                    continue
                if var_case <= 0 or var_case >= 4:
                    print("Ви ввели неіснуючий варіант проведення аналізу.")
                    print("Спробуйте це раз")
                    continue
                if var_case == 3:
                    print("Вихід з меню \"Пошук по критеріях\"")
                    break

                if var_case == 1:
                    count_of_books_by_genre()
                if var_case == 2:
                    count_of_books_by_year()


main()