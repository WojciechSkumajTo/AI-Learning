Kurs nauki AI Neural Networks: Zero to Hero

[LINK]
https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ


Czym jest propagacja wsteczna? Algorytm, który efektywnie pozwala ocenić gradient
pewnego rodzaju funkcji straty do wag sieci neuronowej pozwala nam wtedy iteracyjnie
dostosować wagi do sieci neuronowej aby zminimalizować funkcję straty a tym samym
poprawić dokładność sieci.

Sieci neuronowe to wyrażenia matematyczne --> przyjmują dane wejściowe przyjmują
wagi sieci neuronowej i jest to wyrażenie matematyczne a wynikiem są przewidywania
twojej sieci neuronowej

n-wymiarowymi tensorami, których można używać w nowoczesnych bibliotekach
głębokich sieci (zrozumieć i refaktoryzować propagację wsteczną)
natomiast matematyczne zmiany nie zachodzą.
Tensor - to tablica skalaru

Mikrograd to podstawa tego jak działają sieci neuronowe a inne biblioteki wykorzystują
tę samą mateamtykę natomiast są używane ze względu na wydajność.


https://en.wikipedia.org/wiki/Derivative



Podsumowanie
Sieci neuronowe to wyrażenia matematyczne, które pobierają dane wejściowe jako dane
i pobierają wagi i parametry sieci neuronowej dla przejścia w przód po którym następuje
funkcja straty a funkcja straty próbuje zmierzyć dokładność przewidywań i zazwyczaj
strata będzie niska gdy przewidywania odpowaidają celom lub gdy sieć zachowuje się
dobrze wiec manipulujemy funckją straty tak, że strata jest niska sieć robi to
czego od niej oczekujesz następnie cofamy stratę korzystając z propagacji wstecznej
aby uzyskać gradient i wtedy wiemy jak dostroić wszystkie parametry aby lokalnie
zmniejszyć straty ale wtedy musimy powtarzać ten proces w ramch tak zwanego opadania
gradientu wiec po prosut podążamy za informacjami o gradiencie co minimalizuje straty

