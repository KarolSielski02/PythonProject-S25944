_1 - Wyjaśnienie, dlaczego zastosowane w programie metody są dostosowane do
wybranego typu danych i prezentowanego zagadnienia analitycznego._

**data_loader:**

Moduł ten jest odpowiedzialny za wczytywanie danych z różnych źródeł.
Wczytanie danych to kluczowy pierwszy krok w każdym procesie analizy danych.
Przykładowe metody mogą obejmować wczytywanie danych z plików CSV, baz danych, API, itp.

- Efektywność: Użycie odpowiednich bibliotek (np. pandas) pozwala na szybkie i efektywne wczytanie dużych zestawów danych.

**data_analyzer:**

Ten moduł zawiera metody do analizy danych, takie jak wybór kolumn, filtrowanie, sortowanie, grupowanie i tworzenie grup wiekowych. 
Oto kilka kluczowych metod i ich zastosowanie:

- select_fields_data(data, columns): Wybór konkretnych kolumn z danych.
- filter_data(data, column, value): Filtrowanie danych według określonej wartości w danej kolumnie.
- sort_data(data, column): Sortowanie danych według określonej kolumny.
- remove_na_from_column(data, column_name): Usuwanie brakujących wartości z określonej kolumny.
- convert_categorical_to_numeric(data, column): Konwersja wartości kategorycznych na numeryczne.

	
- Precyzyjność: Pozwalają na dokładne przygotowanie danych do analizy poprzez wybór i filtrowanie odpowiednich informacji.
- Jakość danych: Usuwanie brakujących wartości i konwersja danych kategorycznych poprawia jakość danych, co jest kluczowe dla dalszej analizy.
- Analiza eksploracyjna: Grupowanie i sortowanie danych umożliwia łatwe zrozumienie struktury danych i identyfikację wzorców.

**data_visualizer:**

Moduł ten zajmuje się wizualizacją danych, co jest kluczowym elementem prezentacji wyników analizy. Oto przykłady metod:

- plot_age_distribution(): Tworzy wykres rozkładu wieku.
- plot_gender_distribution(): Wizualizuje rozkład płci.
- plot_work_type_distribution(): Tworzy wykres rozkładu typów pracy.
- plot_pair_plot(fields, hue): Tworzy wykres par wybranych pól.


- Zrozumiałość: Wizualizacje pomagają w łatwiejszym zrozumieniu danych i wyników analizy.
- Komunikacja: Graficzne przedstawienie wyników jest bardziej przystępne dla szerokiego grona odbiorców.
- Identyfikacja wzorców: Wykresy umożliwiają szybkie rozpoznanie wzorców i trendów w danych.

**main.py:**

Główny moduł uruchamia interfejs użytkownika programu (ProgramUi), który integruje wszystkie wcześniej opisane funkcje.

- Integracja: Pozwala na uruchomienie wszystkich modułów w spójny sposób, co umożliwia kompleksową analizę danych i prezentację wyników.

**_Podsumowanie_**

Zastosowane metody w programie są dostosowane do wybranego typu danych i prezentowanego zagadnienia analitycznego, ponieważ:

- Umożliwiają elastyczne i efektywne wczytywanie danych.
- Zapewniają dokładne przygotowanie i czyszczenie danych.
- Ułatwiają analizę eksploracyjną i statystyczną.
- Pozwalają na tworzenie przejrzystych i informacyjnych wizualizacji.

Dzięki temu program może skutecznie przetwarzać, analizować i prezentować dane, co jest kluczowe dla wyciągania wartościowych wniosków analitycznych.

_2 - Wyjaśnienie, dlaczego zastosowane w programie metody są dostosowane do
wybranego typu danych i prezentowanego zagadnienia analitycznego._

Program jest zbudowany z kilku modułów: data_loader.py, data_analyzer.py, data_visualizer.py, new_program_ui.py oraz main.py. Każdy moduł
ma swoją określoną rolę, a ich struktura oraz wzajemne relacje zostały zaprojektowane w sposób ułatwiający realizację 
zadania analitycznego. Poniżej znajdują się szczegółowe wyjaśnienia dotyczące zastosowanych rozwiązań programistycznych.

1. Struktura modułów

Program został podzielony na moduły zgodnie z zasadą pojedynczej odpowiedzialności (ang. Single Responsibility Principle),
co ułatwia zarządzanie kodem i jego dalszy rozwój. Każdy moduł ma jasno zdefiniowaną odpowiedzialność:

- data_loader.py: Wczytywanie danych.
- data_analyzer.py: Analiza danych.
- data_visualizer.py: Wizualizacja danych.
- new_program_ui.py: Generowanie UI.
- main.py: Główny moduł uruchamiający program i integrujący pozostałe moduły.

2. Klasy i ich relacje

Główne klasy znajdują się w modułach data_analyzer.py i data_visualizer.py. Oto ich struktura i relacje:

- DataAnalyzer: Klasa odpowiedzialna za przeprowadzanie różnych operacji analitycznych na danych.
  - Metody takie jak select_fields_data, filter_data, sort_data są statycznymi metodami, co oznacza, że mogą być używane bez konieczności tworzenia instancji klasy. Dzięki temu kod jest bardziej modularny i elastyczny.
  - Klasa ta zawiera także metody do przetwarzania danych, takie jak remove_na_from_column, convert_categorical_to_numeric, które przygotowują dane do dalszej analizy.
- DataVisualizer: Klasa odpowiedzialna za tworzenie wizualizacji danych.
  - Metody tej klasy tworzą różnorodne wykresy, co pozwala na graficzne przedstawienie wyników analizy.
  - Klasa ta korzysta z biblioteki seaborn oraz matplotlib, co pozwala na tworzenie estetycznych i informacyjnych wykresów.
- ProgramUi: Klasa zarządzająca interfejsem użytkownika, która umożliwia interakcję użytkownika z programem.
  - Zastosowano tutaj bibliotekę tkinter do tworzenia interfejsu graficznego. Dzięki temu użytkownik może łatwo wybierać i wyświetlać różne wizualizacje danych.
  - Klasa ta integruje funkcjonalności DataLoader oraz DataVisualizer, umożliwiając wczytywanie danych i ich wizualizację poprzez GUI.

3. Integracja modułów

W module main.py znajduje się główna funkcja programu, która integruje wszystkie pozostałe moduły:

   def main():

   app = ProgramUi()

   app.run_ui()

   if __name__ == '__main__':

   main()`

- ProgramUi: Klasa zarządzająca interfejsem użytkownika, która umożliwia interakcję użytkownika z programem. Pozwala to na
uruchamianie analiz i wizualizacji w sposób zorganizowany i przyjazny dla użytkownika.

4. Zastosowane wzorce projektowe

- Pojedyncza odpowiedzialność (Single Responsibility Principle): Każdy moduł ma jasno zdefiniowaną odpowiedzialność, co zwiększa czytelność kodu i ułatwia jego utrzymanie.
- Stosowanie metod statycznych: Metody w klasie DataAnalyzer są statyczne, co pozwala na ich użycie bez tworzenia instancji klasy. Ułatwia to korzystanie z tych metod w różnych częściach programu.
- Modularność: Program jest podzielony na niezależne moduły, co ułatwia jego rozwijanie i testowanie.

5. Użyte biblioteki i narzędzia

- Pandas: Do manipulacji i analizy danych, co pozwala na efektywne zarządzanie dużymi zbiorami danych.
- Matplotlib i Seaborn: Do tworzenia wykresów i wizualizacji danych, co umożliwia prezentację wyników analizy w przystępnej formie graficznej.
- Tkinter: Do tworzenia interfejsu graficznego, co umożliwia łatwą interakcję użytkownika z programem.

Podsumowanie

Zastosowane rozwiązania programistyczne, w tym struktura modułów, użycie klas i metod statycznych, a także modularność programu,
są odpowiednie dla realizacji zadania analitycznego. Program został zaprojektowany w sposób przejrzysty i elastyczny, 
co umożliwia łatwe wczytywanie, przetwarzanie, analizowanie oraz wizualizowanie danych. Dzięki zastosowaniu odpowiednich wzorców projektowych i 
bibliotek, kod jest łatwy do utrzymania i rozwoju, a wyniki analizy są prezentowane w sposób czytelny i informacyjny. Interfejs użytkownika stworzony przy 
użyciu tkinter umożliwia łatwą i intuicyjną interakcję z programem.