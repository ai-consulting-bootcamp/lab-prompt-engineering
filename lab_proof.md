# Prompt Engineering Lab

## Code en bewijs
[Notebook met prompts, tests en uitvoer](prompt_engineering_lab.ipynb)

## Aanpak
Ik verbeterde prompts voor sentimentanalyse, productbeschrijvingen
en gegevensextractie. Ik gebruikte expliciete uitvoerformaten,
beperkingen, voorbeelden en een stapsgewijze controle-instructie.

## Resultaten
| Taak | Test | Resultaat |
|---|---|---|
| Sentiment | Negatief label, twee regels, beschrijving maximaal 15 woorden | 15/15 |
| Productbeschrijving | Vier regels, juiste valuta, geen onbevestigde eigenschappen | 15/15 |
| Extractie vóór laatste verbetering | Automatische veldcontroles | 12/15 |
| Extractie na laatste verbetering | Dezelfde automatische veldcontroles | 15/15 |

De extractiecontrole test negen velden en de verwachte waarden voor
klantnummer, artikelnummer, datum, categorie en team.
De feedbackteksten en voorgestelde acties vragen daarnaast menselijke controle.

## Voorbeeldinvoer
Hi, I received item 67890. Delivery was two days late,
but the product works perfectly and the packaging was intact.

## Vastgelegde voorbeeldoutput
clientid=Not provided
itemnumber=67890
date=Not provided
delivery_feedback=two days late
product_feedback=works perfectly
packaging_feedback=intact
category=delivery
suggested_team=logistics
proposed_action=Review the delivery process.

## Fouten en beperkingen
Eerdere productprompts verzonnen eigenschappen of veranderden de valuta.
Extractie gebruikte soms een verzonnen jaar of een vraagteken voor een
ontbrekende datum. Expliciete regels en voorbeelden verbeterden de uitvoer.

De percentages gelden voor de geteste invoer en controles.
Ze bewijzen geen algemene betrouwbaarheid. De afzonderlijke bijdrage
van voorbeelden is niet geïsoleerd gemeten.

## Taakvariaties
- Positieve speakerfeedback: correct als positive geclassificeerd.
- Alleen een ordernummer: correct als neutral geclassificeerd.
- Bedrade hoofdtelefoon: EUR 24.50 en 4 werkdagen correct behouden.
- Extractie is ook getest met andere datums en ontbrekende gegevens.

Dit zijn afzonderlijke variatietests, geen meting van algemene nauwkeurigheid.