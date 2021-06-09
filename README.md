# Minesweeper

## Opis Zadania

<ul>  
<li>Główne okno (dalej jako menu) zawiera cztery przyciski:
 <ul>  
<li>Beginner - odświeża menu i tworzy pole dla gry o parametrach: długość - 9, szerokość - 9 (przycisków), min - 10,</li>  
<li>Intermediate - robi to samo tylko o parametrach: długość - 16, szerokość - 16 (przycisków), min - 40,</li>  
<li>Expert - robi to samo, tylko o parametrach: długość - 16, szerokość - 30 (przycisków), min - 99,</li>
<li>Сustom - robi to samo, tylko pobiera informacje z trzech pól tekstowych (height, width, mines) o podanych użytkownikowi parametrach (domyślnie długość - 16, szerokość - 30 (przycisków), min - 145).</li>
<ul><ul><ul><a href="https://ibb.co/TgzqvtW"><img src="https://i.ibb.co/YLvTRh0/4Btn.gif" width=200></a></ul></ul></ul>
</ul>  </li> 
<li>Wprowadzenie mniejszego rozmiaru planszy niż 5x5, powoduje wyświetlenie komunikatu o blędzie. Nie można rozpocząć gry dopóki te parametry nie są poprawne. W przypaku podania za dużej liczby min, program tworzy nową grę i oblicza liczbe min za folmulą `len(height) * len(width) - 1` </li> 
<ul><ul><ul><ul><a href="https://imgbb.com/"><img src="https://i.ibb.co/qyHmBWT/error.gif" alt="error" border="0"></a></ul></ul></ul></ul>
<li>Na początku gry na losowych polach umieszczane jest tyle min ile wskazano w polu
tekstowym lub w zależności od poziomu trudności.</li> 
<li>Na górze programu znajdują się następujące widgety: </li> 
 <ul>  
 <li>Przycisk Menu (lub ESC) - który konczy grę i wraca do menu,</li> 
  <li>Przycisk NG (New Game) - który zaczyna nową gre,</li> 
   <li>Etykieta która pokazuje ile pozostało min do dezaktywacji. </li> 
 </ul>  
<li>Po kliknięciu lewym przyciskiem na pole:</li>
<ul>  
<li>Jeśli w tym polu znajduje się mina, wyświetlana na dole jest wiadomość o przegranej grze, a następnie pokazuje wszystkie miny które pozostały do dezaktywacji (czerwonym kolorem) i gra się kończy,</li>  
<li>Jeśli w sąsiedztwie pola są miny, na przycisku wyświetlana jest ich liczba a pole dezaktywuje się,</li>  
<li>Jeśli wartość pola (min w sąsiedztwie) wynosi zero, to rekurencyjnie bedą otwierane i dezaktywowane najblizsze pola, które mają  w sąsiedztwie chociaż jedną minę.</li>  
<ul><ul><ul><ul><a href="https://ibb.co/pdfpcYW"><img src="https://i.ibb.co/bXsnTcH/leftBtn.gif" alt="leftBtn" width=200></a></ul></ul></ul></ul>
</ul>  
</li>  
<li>Po kliknięciu prawym przyciskiem na pole, zmienia tło na zielone, co program rozumie to jako "jest tu mina", i etykieta obniża watość o jeden. W przypadku kliknięcia prawym przyciskiem na pole które już ma zielone tło, program zwróci poprzednie tło i etykieta zwiększa watość min do dezaktywacji o jeden</li>  
<ul><ul><ul><ul><ul><a href="https://ibb.co/RPzM2tF"><img src="https://i.ibb.co/hHDnsr6/rightBtn.gif" alt="rightBtn" width=200></a></ul></ul></ul></ul></ul>
<li>Gra kończy się po kliknięciu wszystkich pól bez min, lub oznaczeniu "tu jest mina", i program wywietla o tym na dole wiadomość.</li>  
</ul>

## Testy
 1. **test_Input_String** - ten test probuje rozpocząć gre w trybie "Custom" podając litery. 
 2. **test_Input_Invalid_Data** - ten test probuje rozpocząć gre w trybie "Custom" podając niepoprawne wartośći. 
 3. **test_Empty_Input**- ten test probuje rozpocząć gre w trybie "Custom" nie podając żadnych wartośći. 

