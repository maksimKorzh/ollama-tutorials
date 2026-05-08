from pydantic import BaseModel
from ollama import chat
import json

apartment1 = 'Przestronne i funkcjonalne 3 pokojowe mieszkanie o metrażu 49,7m2 na 2 piętrze, wśród zieleni, z dala od hałasu, blisko komunikacji miejskiej, dobry wyjazd na Hallera!!!! , Dorota Panasiuk Licencja 22186, Serdeczne polecam!, Chętnie Państwu odpowiem na dodatkowe pytania i szczegóły, które mogą być dla Państwa ważne., Budynek z cegły z lat 30tych XX wieku.,  Tylko dwa mieszkania na piętrze., Mieszkanie do własnej aranżacji. Okna wychodzą na wschodnią i zachodnia stronę dzięki czemu mieszkanie jest bardzo ciepłe. , Wszystkie media miejskie: ogrzewanie i ciepła woda.,  Wymienione piony wodno-kanalizacyjne. Na podłodze drewno, część okien wymienionych na nowe PCV. Atutem na pewno będzie 12metrowa piwnica.  , Mieszkanie składa się z;, - salonu (ok.16m2), - dwóch pokoi ( ok 13m2, ok 7m2), - kuchni z oknem (ok 6m2), - łazienki z oknem ( ok 4m2), - przedpokoju (ok 4m2),  , Super lokalizacja!!!,  Rejon z rozwiniętą infrastrukturą, wiele sklepów i usług, zadbany skwer tuż pod domem. Blisko przedszkola, szkoły, renomowane lica, uczelnie., Świetny dojazd do centrum, Rynku, Uczeni, jaki w każdą stronę Wrocławia ( tramwaje i autobusy z Ronda Powstańców Śląskich czy Hallera)., Ceniona lokalizacja, idealna oferta dla pary, młodej rodziny jak i dla studenta i inwestora., Lokal odrębna własność, KW bez obciążeń, Licencjonowany Pośrednik w obrocie nieruchomościami z wieloletnim doświadczeniem- Dorota Panasiuk- Licencja nr 22186, kontakt, 885 545 250, Zachęcam do kontaktu i umówienia się na bezpłatna prezentację-- SERDECZNIE ZAPRASZAM do zapoznania się z interesującą ofertą., Zamieszczona oferta nie stanowi oferty w rozumieniu Kodeksu Cywilnego, a dane w nich zawarte mają jedynie charakter informacyjny.'

# {
#   "street_address": "",
#   "build_year": 1930,
#   "floor": 2,
#   "area": 49.7,
#   "bedrooms": 3,
#   "amenities": [
#     "Central heating",
#     "Hot water supply",
#     "New PVC windows in some areas"
#   ]
# }

apartment2 = 'Poszukujesz mieszkania w doskonałej lokalizacji dla siebie, kogoś bliskiego lub inwestycyjnie? Sprawdź tą ofertę dla Ciebie., 5 min ! pieszo - Uniwersytet Przyrodniczy !, 10-15 min ! pieszo - UMCS oraz Politechnika Lubelska !, OPIS NIERUCHOMOŚCI , Ofertę stanowi mieszkanie o powierzchni 30,68 m2, położone przy ul. Glinianej 27, w dzielnicy LSM Lublin. , Nieruchomość zlokalizowana jest w świetnej lokalizacji - LSM to dzielnica uniwersytecka nastawiona na obsługę miejscowych studentów, dzięki temu usługi, czy komunikacja są tu bardzo dobrze rozwinięte. Mieszkanie sprawdzi się idealnie pod najem, a także do zamieszkania dla singla lub osoby starszej. Pod blokiem ogólnodostępne miejsca parkingowe. Spokojne, przyjazne i zielone osiedle dla każdego. , Ekspozycja okien: kuchnia i pokój - północny-wschód, z piękną panoramą za oknami., W skład rozkładowego mieszkania wchodzą: , - sypialnia o pow. ok. 16,15 m2, - osobna kuchnia o pow. ok. 7,83 m2, - łazienka z WC o pow. ok. 3 m2, - korytarz o pow. ok. 3,7 m2, Rzut mieszkania załączony w zdjęciach. Wymiaru pomieszczeń nie są podane z rzeczywistą dokładnością, lecz są wartościami zaokrąglonymi. , W pobliżu sklepy spożywcze, uczelnie wyższe, poczta, stomatologia, restauracje, szpital, przedszkole, szkoła podstawowa, kościół itp. Wszystkie najważniejsze usługi w sąsiedztwie. Wiele miejsc na spacer, czy rekreacje: ścieżki piesze i rowerowe. Świetne połączenie komunikacyjne samochodowe jak i przez transport publiczny MPK, zlokalizowany zaledwie 5 min. pieszo., STAN PRAWNY, Pełna własność, Księga Wieczysta bez obciążeń., KOSZTY UTRZYMANA, Woda z wodociągu miejskiego, ogrzewanie z sieci miejskiej, ciepła woda z piecyka gazowego (nowy), Czynsz administracyjny kształtuje się na poziomie ok. 353 zł. Opłaty za prąd, gaz - według zużycia. , CHCESZ TU ZAMIESZKAĆ? , Mieszkanie można obejrzeć po uprzednim umówieniu się na konkretną godzinę., Ze względów bezpieczeństwa przed spotkaniem związanym z prezentacją będziemy Państwa prosić o podanie danych personalnych oraz o złożenie czytelnego podpisu na dokumentach potwierdzających chęć obejrzenia nieruchomości., CENA OFERTOWA , 349 000,00 zł , Nie szukaj dalej. Zadzwoń! , Oferta na wyłączność biura nieruchomości ONESTO BROKER., OPIEKUN OFERTY, Jolanta Wach, 781 208 610 , e-mail: wach@, Licencjonowany Pośrednik Nieruchomości, Informacja o kosztach transakcji: Do ceny nieruchomości należy doliczyć koszty notarialne, podatek PCC oraz koszty obsługi transakcji. , KREDYT HIPOTECZNY , Rozważasz kredytowanie tej nieruchomości? Pomożemy w uzyskaniu kredytu hipotecznego na najlepszych warunkach. Mamy do wyboru oferty kredytowe praktycznie wszystkich banków. Będziesz mógł dowolnie je porównać i to bez żadnych zobowiązań. , Opis oferty sporządzony został na podstawie informacji pochodzących od właściciela oferującego nieruchomość, dokumentów opisujących jej stan prawny i przeprowadzonych oględzin. Opis ten może podlegać aktualizacji oraz nie stanowi oferty handlowej określonej w art. 66 i następnych K.C, Treść niniejszego ogłoszenia nie stanowi oferty handlowej w rozumieniu Kodeksu Cywilnego., Oferta wysłana z programu IMO dla biur nieruchomości'

# {
#   "street_address": "ul. Glinianej 27",
#   "build_year": 0,
#   "floor": 0,
#   "area": 30.68,
#   "bedrooms": 1,
#   "amenities": [
#     "parking spaces nearby",
#     "quiet and friendly neighborhood",
#     "nearby shops and services",
#     "university area with good infrastructure for students",
#     "multiple walking and cycling paths",
#     "good public transportation connection via MPK",
#     "nearby medical facilities",
#     "nearby schools and preschools",
#     "church nearby",
#     "new gas water heater"
#   ]
# }

class Apartment(BaseModel):
  street_address: str
  build_year: int
  floor: int
  area: float
  bedrooms: int # bedrooms instead of rooms to reduce hallucination
  amenities: list[str]
  
response = chat(
  model='qwen2.5',
  messages=[{'role': 'user', 'content': apartment2}],
  format=Apartment.model_json_schema(),
)

print(json.dumps(json.loads(response.message.content), indent=2))
