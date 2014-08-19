#!/usr/bin/env python
# encoding: utf-8
import json
import requests
from time import sleep
import sys

start = raw_input('To start the import type YES: ')
if start != 'YES':
    sys.exit(0)


data_dict = [
  {
    "name": "Amir Sandwich",
    "offerings": "options",
    "comment": "Falafel-Imbiss",
    "lookup_address": "Paradiesgasse 46 Frankfurt am Main",
    "phone_number": "+49-69-623333",
    "websites": [{"url": "https://www.facebook.com/pages/Amir-Sandwich/200867749939725", "kind": "facebook"}]
  },
  {
    "name": "Apfelwein JB Handlung",
    "offerings": "options",
    "comment": "Veganer Apfelwein",
    "lookup_address": "Brückenstraße 21 Frankfurt am Main",
    "phone_number": "+49-176-35424235",
    "websites": [{"url": "http://www.apfelweinhandlung.de", "kind": "website"}]
  },
  {
    "name": "Arche Nova",
    "offerings": "options",
    "comment": "Leider gab es in der Vergangenheit einige 'Unfälle', d.h. Fleisch oder Butter in vegan deklarierten Speisen.",
    "lookup_address": "Kasseler Straße 1a Frankfurt am Main",
    "phone_number": "+49-69-7075859",
    "websites": [{"url": "http://restaurant-archenova.de/node/36", "kind": "website"}]
  },
  {
    "name": "Aroma",
    "offerings": "options",
    "comment": "Falafel-Imbiss",
    "lookup_address": "Adlerflychtplatz Frankfurt am Main",
    "phone_number": "+49-69-25717546",
    "websites": [{"url": "http://aromaffm.com", "kind": "website"}]
  },
  {
    "name": "Aroydee",
    "offerings": "options",
    "comment": "Thailändisch",
    "lookup_address": "Stiftstraße 34 Frankfurt am Main",
    "phone_number": "+49-69-29723636",
    "websites": [{"url": "http://www.aroydee.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Aroydee-thailändische-original-Küche/357007734392797", "kind": "facebook"}]
  },
  {
    "name": "Bäcker Kahl",
    "offerings": "options",
    "lookup_address": "Friedberger Anlage 14 Frankfurt am Main",
    "phone_number": "+49-69-439876",
    "websites": [{"url": "http://www.baecker-kahl.de", "kind": "website"}]
  },
  {
    "name": "Bergstation",
    "offerings": "options",
    "comment": "Befindet sich im Huthpark",
    "lookup_address": "Propst-Goebels-Weg 17 Frankfurt am Main",
    "phone_number": "+49-69-47881499",
    "websites": [{"url": "http://www.bergstation-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/BERGstation-CaféRestaurant-im-Huthpark/295309850583487", "kind": "facebook"}]
  },
  {
    "name": "Biospahn-Vegan",
    "offerings": "vegan",
    "comment": "veganer Imbiss",
    "lookup_address": "Berger Straße 222 Frankfurt am Main",
    "phone_number": "+49-69-455481",
    "websites": [{"url": "http://biospahn-vegan.de", "kind": "website"}, {"url": "http://www.facebook.com/biospahnVegan", "kind": "facebook"}]
  },
  {
    "name": "Café Alex",
    "offerings": "options",
    "lookup_address": "Bergerstraße 206 Frankfurt am Main",
    "phone_number": "+49-69-94508853",
    "websites": [{"url": "https://www.facebook.com/pages/Café-Alex/487239511314404", "kind": "facebook"}]
  },
  {
    "name": "Café Lounge Jasmin",
    "offerings": "options",
    "lookup_address": "Alt Fechenheim 94 Frankfurt am Main",
    "phone_number": "+49-69-26956584",
    "websites": [{"url": "http://www.cafe-jasmin-lounge.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Café-Jasmin-Lounge/170787139655671", "kind": "facebook"}]
  },
  {
    "name": "Cafe Metropol",
    "offerings": "options",
    "lookup_address": "Weckmarkt 15 Frankfurt am Main",
    "phone_number": "+49-69-288287",
    "websites": [{"url": "http://www.metropolcafe.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Cafe-Metropol/134688509896070", "kind": "facebook"}]
  },
  {
    "name": "Chez Ima",
    "offerings": "options",
    "lookup_address": "Niddastraße 58 Frankfurt am Main",
    "phone_number": "+49-69-256677280 ",
    "websites": [{"url": "http://www.imaworld.de/#speisekarte_chez", "kind": "website"}]
  },
  {
    "name": "Chidoba - Mexican Grill",
    "offerings": "options",
    "lookup_address": "Nidacorso 5 Frankfurt am Main",
    "phone_number": "+49-69-47866516",
    "websites": [{"url": "http://www.chidoba.com", "kind": "website"}, {"url": "https://www.facebook.com/Chidoba", "kind": "facebook"}]
  },
  {
    "name": "Chimichurri",
    "offerings": "vegan",
    "comment": "Täglich wechselnde Karte. Getränke zum Teil noch nicht vegan.",
    "lookup_address": "Im Prüfling 63 Frankfurt am Main",
    "phone_number": "+49-69-13825299",
    "websites": [{"url": "http://www.chimichurri-frankfurt.de", "kind": "website"}, {"url": "http://www.facebook.com/chimichurrifrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Cigköftem Frankfurt",
    "offerings": "options",
    "comment": "Türkischer Imbiss",
    "lookup_address": "Münchener Straße 20 Frankfurt am Main",
    "phone_number": "+49-69-36602372",
    "websites": [{"url": "https://www.facebook.com/pages/Cigköftem-Frankfurt/227085597373757", "kind": "facebook"}]
  },
  {
    "name": "Coa Frankfurt Schillerstraße",
    "offerings": "options",
    "lookup_address": "Schillerstraße 4 Frankfurt am Main",
    "phone_number": "+49-6992039966",
    "websites": [{"url": "http://www.coa.as/", "kind": "website"}]
  },
  {
    "name": "Coa Myzeil",
    "offerings": "options",
    "lookup_address": "Zeil 106 Frankfurt am Main",
    "phone_number": "+49-6921657824",
    "websites": [{"url": "http://www.coa.as/", "kind": "website"}]
  },
  {
    "name": "Coa Skyline Plaza",
    "offerings": "options",
    "lookup_address": "Europa Allee 6 Frankfurt am Main",
    "phone_number": "+49-69-27292818",
    "websites": [{"url": "http://www.coa.as/", "kind": "website"}]
  },
  {
    "name": "Cuccis",
    "offerings": "options",
    "comment": "Bahnsteig 6/7, 8/9, 12/13",
    "lookup_address": "Hauptbahnhof Frankfurt am Main",
    "websites": [{"url": "http://www.cuccis.de", "kind": "website"}, {"url": "https://www.facebook.com/cuccisfood", "kind": "facebook"}]
  },
  {
    "name": "DasEis",
    "offerings": "options",
    "lookup_address": "Hasengasse 1 Frankfurt am Main",
    "phone_number": "+49-69-74731409",
    "websites": [{"url": "http://facebook.com/pages/DasEis/154140254618730", "kind": "facebook"}]
  },
  {
    "name": "Das Leben ist schön",
    "offerings": "options",
    "lookup_address": "Hanauer Landstraße 198 Frankfurt am Main",
    "phone_number": "+49-69-43057870",
    "websites": [{"url": "http://www.daslebenistschoen.de", "kind": "website"}, {"url": "https://www.facebook.com/DasLebenIstSchoenFFM", "kind": "facebook"}]
  },
  {
    "name": "Dean & David (Kaiserstraße)",
    "offerings": "options",
    "comment": "Bieten auch einen Lieferservice",
    "lookup_address": "Kaiserstraße 31 Frankfurt am Main",
    "phone_number": "+49-69-80088363",
    "websites": [{"url": "http://deananddavid.de", "kind": "website"}, {"url": "http://deananddavid.de/wp-content/uploads/2008/10/Allergenfibel-01-2012.pdf", "kind": "menu"}]
  },
  {
    "name": "Dean & David (An der Welle)",
    "offerings": "options",
    "comment": "Bieten auch einen Lieferservice",
    "lookup_address": "An der Welle 4 Frankfurt am Main",
    "phone_number": "+49-69-66056688",
    "websites": [{"url": "http://deananddavid.de", "kind": "website"}, {"url": "http://deananddavid.de/wp-content/uploads/2008/10/Allergenfibel-01-2012.pdf", "kind": "menu"}]
  },
  {
    "name": "Die Kuh, die lacht (Schillerstraße)",
    "offerings": "options",
    "lookup_address": "Schillerstraße 28 Frankfurt am Main",
    "phone_number": "+49-69-27290171",
    "websites": [{"url": "http://www.diekuhdielacht.com", "kind": "website"}, {"url": "https://www.facebook.com/diekuhdielacht", "kind": "facebook"}]
  },
  {
    "name": "Die Kuh, die lacht (Friedensstraße)",
    "offerings": "options",
    "lookup_address": "Friedensstraße 2 Frankfurt am Main",
    "phone_number": "+49-69-15342987",
    "websites": [{"url": "http://www.diekuhdielacht.com", "kind": "website"}, {"url": "https://www.facebook.com/diekuhdielacht", "kind": "facebook"}]
  },
  {
    "name": "Döpfner's im Maingau",
    "offerings": "options",
    "comment": "Catering",
    "lookup_address": "Schifferstraße 38 Frankfurt am Main",
    "phone_number": "+49-69-60914289",
    "websites": [{"url": "http://maingau.de/de/restaurant", "kind": "website"}, {"url": "https://www.facebook.com/DoepfnersImMaingau", "kind": "facebook"}]
  },
  {
    "name": "Dulce Chocolate & Ice Cream",
    "offerings": "options",
    "comment": "Veganes Eis wie Mango, Maracuja, Erdbeere, Sauerkirsch. Nur natürliche Zutaten.",
    "lookup_address": "Schweizer Straße 43 Frankfurt am Main",
    "phone_number": "+49-69-60627968",
    "websites": [{"url": "http://www.dulce-chocolate.com/de", "kind": "website"}, {"url": "https://www.facebook.com/dulcechocolateandicecream", "kind": "facebook"}]
  },
  {
    "name": "Echt",
    "offerings": "options",
    "comment": "Gutbürgerlich (z.b. Schnitzel), info@echt-frankfurt.de",
    "lookup_address": "Berger Straße 319 Frankfurt am Main",
    "phone_number": "+49-175-9979500",
    "websites": [{"url": "http://echt-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/echt.frankfurt", "kind": "facebook"}]
  },
  {
    "name": "Edelkiosk",
    "offerings": "vegan",
    "comment": "Veganes Café",
    "lookup_address": "Rhönstraße 119 Frankfurt am Main",
    "phone_number": "+49-69-47862404",
    "websites": [{"url": "http://www.edelkiosk.de", "kind": "website"}, {"url": "http://www.facebook.com/edelkiosk", "kind": "facebook"}]
  },
  {
    "name": "Eis Christina",
    "offerings": "options",
    "lookup_address": "Eckenheimer Landstraße 78 Frankfurt am Main",
    "phone_number": "+49-69-598452",
    "websites": [{"url": "http://www.eischristina.de", "kind": "website"}, {"url": "https://www.facebook.com/eischristina", "kind": "facebook"}]
  },
  {
    "name": "El Pacifico",
    "offerings": "options",
    "comment": "Mexikanisch",
    "lookup_address": "Sandweg 79 Frankfurt am Main",
    "phone_number": "+49-69-446988",
    "websites": [{"url": "http://www.el-pacifico-ffm.de", "kind": "website"}, {"url": "http://www.facebook.com/elpacifico.ffm", "kind": "facebook"}]
  },
  {
    "name": "Empanadiso",
    "offerings": "options",
    "lookup_address": "Mainzer Landstraße 112a Frankfurt am Main",
    "phone_number": "+49-69-87203010",
    "websites": [{"url": "http://www.empanadiso.de", "kind": "website"}, {"url": "https://www.facebook.com/Empanadiso", "kind": "facebook"}]
  },
  {
    "name": "Extravegant - Alles aus Liebe",
    "offerings": "vegan",
    "comment": "veganes Café",
    "lookup_address": "Berger Straße 154 Frankfurt am Main",
    "phone_number": "+49-69-27249532",
    "websites": [{"url": "http://www.extravegant-ffm.de", "kind": "website"}, {"url": "https://www.facebook.com/extravegant.allesausliebe", "kind": "facebook"}]
  },
  {
    "name": "Frankfurt and Friends",
    "offerings": "options",
    "lookup_address": "Jordanstraße 1 Frankfurt am Main",
    "phone_number": "+49-69-77075061",
    "websites": [{"url": "http://www.frankfurtandfriends.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Frankfurt-and-Friends/325600730881716", "kind": "facebook"}]
  },
  {
    "name": "Frankfurter Pause",
    "offerings": "options",
    "comment": "Sandwich-Imbiss",
    "lookup_address": "Rossmarkt 10 Frankfurt am Main",
    "websites": [{"url": "https://www.facebook.com/FrankfurterPause", "kind": "facebook"}]
  },
  {
    "name": "Gasthaus zum Bären",
    "offerings": "options",
    "lookup_address": "Höchster Schlossplatz 8 Frankfurt am Main",
    "phone_number": "+49-69-309343",
    "websites": [{"url": "http://www.zumbaeren.net", "kind": "website"}, {"url": "https://www.facebook.com/gasthaus.zum.baeren", "kind": "facebook"}]
  },
  {
    "name": "Gaststätte Bootshaus Fechenheim",
    "offerings": "options",
    "lookup_address": "Fechenheimer Leinpfad 1 Frankfurt am Main",
    "phone_number": "+49-69-90759757",
    "websites": [{"url": "http://www.gaststaette-bootshaus.com", "kind": "website"}, {"url": "https://www.facebook.com/pages/Gaststätte-Bootshaus-Fechenheim/423076294379482", "kind": "facebook"}]
  },
  {
    "name": "Giggle Pea",
    "offerings": "options",
    "lookup_address": "Brüningstraße 17  Frankfurt am Main",
    "phone_number": "+49-69-56996868",
    "websites": [{"url": "http://gigglepea.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Giggle-Pea/376030552482067", "kind": "facebook"}]
  },
  {
    "name": "Ginkgo",
    "offerings": "options",
    "lookup_address": "Berger Straße 81 Frankfurt am Main",
    "phone_number": "+49-69-491202",
    "websites": [{"url": "http://www.ginkgo-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/ginkgoffm", "kind": "facebook"}]
  },
  {
    "name": "Grüneburger Bioladen",
    "offerings": "options",
    "lookup_address": "Grüneburgweg 6 Frankfurt am Main",
    "phone_number": "+49-69-95502229",
  },
  {
    "name": "Grünkern Naturkost",
    "offerings": "options",
    "comment": "Bioladen mit Bistro",
    "lookup_address": "Stegstraße 59 Frankfurt am Main",
    "phone_number": "+49-69-627649",
    "websites": [{"url": "http://www.gruenkern-naturkost.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Grünkern-Naturkost-Bioladen-Bistro/160650967302102", "kind": "facebook"}]
  },
  {
    "name": "Habibi Sandwich Frankfurt",
    "offerings": "options",
    "comment": "Falafel-Imbiss",
    "lookup_address": "Offenbacher Landstraße 1 Frankfurt am Main",
    "phone_number": "+49-69-66575725",
    "websites": [{"url": "http://www.habibisandwich.com", "kind": "website"}, {"url": "https://www.facebook.com/pages/Habibi-Sandwich/148007882064497", "kind": "facebook"}]
  },
  {
    "name": "Heidi und Paul",
    "offerings": "options",
    "lookup_address": "Meisengasse 12 Frankfurt am Main",
    "phone_number": "+49-69-29729828",
    "websites": [{"url": "http://www.heidiundpaul.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Heidi-und-Paul/115930075133334", "kind": "facebook"}]
  },
  {
    "name": "Home Ramen",
    "offerings": "options",
    "comment": "Japanisch",
    "lookup_address": "Pfingstweidstraße 12 Frankfurt am Main",
    "phone_number": "+49-69-40566633",
    "websites": [{"url": "http://www.home-ramen.de", "kind": "website"}]
  },
  {
    "name": "IIMORI",
    "offerings": "options",
    "comment": "Japanisch",
    "lookup_address": "Braubachstraße 24 Frankfurt am Main",
    "phone_number": "+49-69-56999966",
    "websites": [{"url": "http://www.iimori.de", "kind": "website"}, {"url": "http://www.iimori.de/Koestlichkeiten/#/4/", "kind": "menu"}, {"url": "https://www.facebook.com/iimori.de", "kind": "facebook"}]
  },
  {
    "name": "Im Herzen Afrikas",
    "offerings": "options",
    "comment": "Vegetarische Platte ist vegan. (Bitte vegan bestellen, wird sonst mit Butter zubereitet)",
    "lookup_address": "Gutleutstraße 13 Frankfurt am Main",
    "phone_number": "+49-69-24246080",
    "websites": [{"url": "http://im-herzen-afrikas.de", "kind": "website"}, {"url": "http://www.facebook.com/pages/Im-Herzen-Afrikas/61805222589", "kind": "facebook"}]
  },
  {
    "name": "Kaiser Biobäckerei Berger Straße",
    "offerings": "options",
    "lookup_address": "Berger Straße 76 Frankfurt am Main",
    "phone_number": "+49-69-87000260",
    "websites": [{"url": "http://www.ihre-bio-baeckerei.de", "kind": "website"}, {"url": "https://www.facebook.com/KaiserBiobaeckerei", "kind": "facebook"}]
  },
  {
    "name": "Kaiser Biobäckerei Börsenplatz",
    "offerings": "options",
    "lookup_address": "Börsenplatz 1 Frankfurt am Main",
    "phone_number": "+49-69-15342489",
    "websites": [{"url": "http://www.ihre-bio-baeckerei.de", "kind": "website"}, {"url": "https://www.facebook.com/KaiserBiobaeckerei", "kind": "facebook"}]
  },
  {
    "name": "Kaiser Biobäckerei Weserstraße",
    "offerings": "options",
    "lookup_address": "Weserstraße 41 Frankfurt am Main",
    "phone_number": "+49-69-234341",
    "websites": [{"url": "http://www.ihre-bio-baeckerei.de", "kind": "website"}, {"url": "https://www.facebook.com/KaiserBiobaeckerei", "kind": "facebook"}]
  },
  {
    "name": "Kaiser Biobäckerei Eschersheimer Landstraße",
    "offerings": "options",
    "comment": "Befindet sich im Reformhaus Freya",
    "lookup_address": "Eschersheimer Landstraße 248 Frankfurt am Main",
    "phone_number": "+49-69-87001947",
    "websites": [{"url": "http://www.ihre-bio-baeckerei.de", "kind": "website"}, {"url": "https://www.facebook.com/KaiserBiobaeckerei", "kind": "facebook"}]
  },
  {
    "name": "Kaiser Biobäckerei Schweizer Straße",
    "offerings": "options",
    "lookup_address": "Schweizer Straße 68 Frankfurt am Main",
    "phone_number": "+49-69-87001590",
    "websites": [{"url": "http://www.ihre-bio-baeckerei.de", "kind": "website"}, {"url": "https://www.facebook.com/KaiserBiobaeckerei", "kind": "facebook"}]
  },
  {
    "name": "Galleria Kaufhof an der Hauptwache",
    "offerings": "options",
    "comment": "Vegane Einkaufsmöglichkeit im Untergeschoss (Galleria Gourmet)",
    "lookup_address": "Zeil 116 Frankfurt am Main",
    "websites": [{"url": "http://www.galeria-kaufhof.de/filialen/frankfurt-hauptwache", "kind": "website"}]
  },
  {
    "name": "King Creole",
    "offerings": "options",
    "lookup_address": "Eckenheimer Landstraße 346 Frankfurt am Main",
    "phone_number": "+49-69-542172",
    "websites": [{"url": "http://www.kingcreole.de", "kind": "website"}, {"url": "https://www.facebook.com/restaurantkingcreole", "kind": "facebook"}]
  },
  {
    "name": "Kleine Anna",
    "offerings": "options",
    "lookup_address": "Mainzer Landstraße 111 Frankfurt am Main",
    "phone_number": "+49-69-45094894",
    "websites": [{"url": "http://www.kleineanna.de", "kind": "website"}]
  },
  {
    "name": "Labouche",
    "offerings": "options",
    "lookup_address": "Kleiststraße 39 Frankfurt am Main",
    "phone_number": "+49-69-25426288 ",
    "websites": [{"url": "http://labouche-ffm.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/LaBouche/126514730827852", "kind": "facebook"}]
  },
  {
    "name": "Langosch",
    "offerings": "options",
    "lookup_address": "Fahrgasse 3 Frankfurt am Main",
    "phone_number": "+49-69-92039510",
    "websites": [{"url": "http://langosch-am-main.com", "kind": "website"}, {"url": "http://www.facebook.com/LangoschAmMain", "kind": "facebook"}]
  },
  {
    "name": "Laube Liebe Hoffnung",
    "offerings": "options",
    "lookup_address": "Pariser Straße 11 Frankfurt am Main",
    "phone_number": "+49-69-75847722",
    "websites": [{"url": "http://www.laubeliebehoffnung.de", "kind": "website"}, {"url": "https://www.facebook.com/laubeliebehoffnung", "kind": "facebook"}]
  },
  {
    "name": "Lebe Gesund Kleinmarkthalle",
    "offerings": "vegan",
    "comment": "100% vegane Produkte, ohne Tierdung hergestellt.",
    "lookup_address": "Hasengasse 5-7 Frankfurt am Main",
    "phone_number": "+49-69-292936",
    "websites": [{"url": "http://www.lebegesund.de/content/lebe-gesund-laeden-7tkjcvk2h0z-c.htm", "kind": "website"}]
  },
  {
    "name": "Lebe Gesund Nordwestzentrum",
    "offerings": "vegan",
    "comment": "100% vegane Produkte, ohne Tierdung hergestellt.",
    "lookup_address": "Limescorso 8 Frankfurt am Main",
    "phone_number": "+49-69-578941",
    "websites": [{"url": "http://www.lebegesund.de/content/lebe-gesund-laeden-7tkjcvk2h0z-c.htm", "kind": "website"}]
  },
  {
    "name": "Le Crobag",
    "offerings": "options",
    "comment": "Gegenüber Gleis 12",
    "lookup_address": "Am Hauptbahnhof Frankfurt am Main",
    "websites": [{"url": "http://www.lecrobag.de", "kind": "website"}]
  },
  {
    "name": "Lokalbahnhof",
    "offerings": "options",
    "lookup_address": "Darmstädter Landstraße 14 Frankfurt am Main",
    "phone_number": "+49-69-36602966",
    "websites": [{"url": "http://www.lokalbahnhof.info", "kind": "website"}, {"url": "https://www.facebook.com/pages/Lokalbahnhof-Bar/571499796209663", "kind": "facebook"}]
  },
  {
    "name": "Luna Burger",
    "offerings": "options",
    "comment": "Vegane Burger Option",
    "lookup_address": "Schäfergasse 46 Frankfurt am Main",
    "phone_number": "+49-69-21087665",
    "websites": [{"url": "http://luna-burger.de", "kind": "website"}, {"url": "https://www.facebook.com/lunaburger", "kind": "facebook"}]
  },
  {
    "name": "Mamoona Cuisine",
    "offerings": "options",
    "comment": "Marokkanisch-libanesisch. Vegane Vorspeisen und Hauptgerichte.",
    "lookup_address": "Hanauer Landstraße 2 Ostend Frankfurt am Main",
    "phone_number": "+49-69-17427597",
    "websites": [{"url": "http://www.mamoona-cuisine.com", "kind": "website"}, {"url": "https://www.facebook.com/pages/mamoona-cuisine/136277519792190", "kind": "facebook"}]
  },
  {
    "name": "Margarete",
    "offerings": "options",
    "comment": "Sonntags ab 18 Uhr rein vegan",
    "lookup_address": "Braubachstraße 18 Frankfurt am Main",
    "phone_number": "+49-69-13066500",
    "websites": [{"url": "http://www.margarete-restaurant.de", "kind": "website"}, {"url": "https://www.facebook.com/margaretefrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Matildas Kitchen",
    "offerings": "options",
    "lookup_address": "Grüneburgweg 86 Frankfurt am Main",
    "phone_number": "+49-69-71673700",
    "websites": [{"url": "http://www.matildaskitchen.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Matildas-Kitchen/150901071640134", "kind": "facebook"}]
  },
  {
    "name": "Michis Schokoatelier",
    "offerings": "options",
    "lookup_address": "Sandweg 60 Frankfurt am Main",
    "phone_number": "+49-69-40898066",
    "websites": [{"url": "http://www.michis-schokoatelier.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Michis-Schokoatelier/127400360695799", "kind": "facebook"}]
  },
  {
    "name": "Mongo's",
    "offerings": "options",
    "comment": "Mongolisch",
    "lookup_address": "Hanauer Landstraße 291 Frankfurt am Main",
    "phone_number": "+49-69-24240650",
    "websites": [{"url": "http://www.mongos.de", "kind": "website"}, {"url": "https://www.facebook.com/mongos.frankfurt", "kind": "facebook"}]
  },
  {
    "name": "Monkeys Nudels Bar",
    "offerings": "options",
    "lookup_address": "Oeder Weg 2 Frankfurt am Main",
    "phone_number": "+49-69-9550747712",
    "websites": [{"url": "https://www.facebook.com/pages/Monkeys-Nudels-Bar/100672199998220", "kind": "facebook"}]
  },
  {
    "name": "MoschMosch Goetheplatz",
    "offerings": "options",
    "lookup_address": "Goetheplatz 2 Frankfurt am Main",
    "phone_number": "+49-69-27291565",
    "websites": [{"url": "http://www.moschmosch.com", "kind": "website"}, {"url": "https://www.facebook.com/MoschMoschMosch", "kind": "facebook"}]
  },
  {
    "name": "MoschMosch Kaiserstraße",
    "offerings": "options",
    "lookup_address": "Kaiserstraße 13 Frankfurt am Main",
    "phone_number": "+49-69-460904860",
    "websites": [{"url": "http://www.moschmosch.com", "kind": "website"}, {"url": "https://www.facebook.com/MoschMoschMosch", "kind": "facebook"}]
  },
  {
    "name": "MoschMosch Wilhelm-Leuschner-Straße",
    "offerings": "options",
    "lookup_address": "Wilhelm-Leuschner-Straße 78 Frankfurt am Main",
    "phone_number": "+49-69-24003737",
    "websites": [{"url": "http://www.moschmosch.com", "kind": "website"}, {"url": "https://www.facebook.com/MoschMoschMosch", "kind": "facebook"}]
  },
  {
    "name": "Mr. Samosa",
    "offerings": "options",
    "comment": "Indisch",
    "lookup_address": "Bergerstraße 83 Frankfurt am Main",
    "phone_number": "+49-69-90436465",
    "websites": [{"url": "http://www.mrsamosa.de", "kind": "website"}, {"url": "http://www.facebook.com/mrsamosaffm", "kind": "facebook"}]
  },
  {
    "name": "My Indigo",
    "offerings": "options",
    "comment": "Gegenüber Gleis 6",
    "lookup_address": "Am Hauptbahnhof Frankfurt am Main",
    "phone_number": "+49-151-65623567",
    "websites": [{"url": "http://www.einkaufsbahnhof.de/frankfurt-hauptbahnhof/schlemmen/gastronomie/ffm_my-indigo-s6347", "kind": "website"}, {"url": "https://www.facebook.com/myIndigoFrankfurtMarkthalle", "kind": "facebook"}]
  },
  {
    "name": "Naschwerkstatt",
    "offerings": "options",
    "comment": "Shop mit vielen veganen Produkten und Gerichten",
    "lookup_address": "Alte Gasse 27 Frankfurt am Main",
    "phone_number": "+49-69-15629980",
    "websites": [{"url": "http://www.naschwerkstatt.de", "kind": "website"}, {"url": "https://www.facebook.com/Naschwerkstatt", "kind": "facebook"}]
  },
  {
    "name": "Naturbar",
    "offerings": "options",
    "comment": "Vegetarisch-veganes Restaurant",
    "lookup_address": "Oeder Weg 26 Frankfurt am Main",
    "phone_number": "+49-69-554486",
    "websites": [{"url": "http://www.naturbar-frankfurt.de", "kind": "website"}]
  },
  {
    "name": "Nordlicht",
    "offerings": "options",
    "lookup_address": "Koselstraße 2 Frankfurt am Main",
    "phone_number": "+49-69-21008877",
    "websites": [{"url": "http://www.nordlicht-ffm.de", "kind": "website"}, {"url": "https://www.facebook.com/nordlicht.ffm", "kind": "facebook"}]
  },
  {
    "name": "Patel's Euro-Central Cafe",
    "offerings": "options",
    "comment": "Indisch",
    "lookup_address": "Horst-Schulmann-Straße 1 Frankfurt am Main",
    "phone_number": "+49-69-90436410",
    "websites": [{"url": "http://www.patels-eurocentral.de", "kind": "website"}, {"url": "https://www.facebook.com/Patels.EuroCentral", "kind": "facebook"}]
  },
  {
    "name": "Petersen Gutes Essen",
    "offerings": "options",
    "lookup_address": "Eppsteiner Straße 26 Frankfurt am Main",
    "phone_number": "+49-69-71713536",
    "websites": [{"url": "http://petersen-gutes-essen.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Petersen-Gutes-Essen/164737713536713", "kind": "facebook"}]
  },
  {
    "name": "Picknickbank",
    "offerings": "options",
    "comment": "Marokkanisch",
    "lookup_address": "Weissadlergasse 7 Frankfurt am Main",
    "phone_number": "+49-69-92884922",
    "websites": [{"url": "http://www.picknickbank-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Picknickbank/251886254862656", "kind": "facebook"}]
  },
  {
    "name": "Pistazie",
    "offerings": "options",
    "comment": "Persisch & vegetarisch. Auf Wunsch werden alle Speisen vegan zubereitet.",
    "lookup_address": "Baumweg 20 Frankfurt am Main",
    "phone_number": "+49-69-49086001",
    "websites": [{"url": "http://www.pistazie-ffm.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Restaurant-Pistazie/265574826847046", "kind": "facebook"}]
  },
  {
    "name": "Pizzeria Mars",
    "offerings": "options",
    "comment": "Wilmersburger Pizzaschmelz",
    "lookup_address": "Victor-Slotosch-Straße 6 Frankfurt am Main",
    "phone_number": "+49-6109699920",
    "websites": [{"url": "http://www.mars-pizza.de", "kind": "website"}, {"url": "https://www.facebook.com/MarsPizzeria", "kind": "facebook"}]
  },
  {
    "name": "Pizzeria Olbia",
    "offerings": "options",
    "lookup_address": "Glauburgstraße 14 Frankfurt am Main",
    "phone_number": "+49-69-5972925",
    "websites": [{"url": "http://www.pizzeriaolbia.de", "kind": "website"}, {"url": "https://www.facebook.com/pizzeriaolbiafrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Punjabi Kitchen",
    "offerings": "options",
    "comment": "Indischer Lieferservice",
    "lookup_address": "Im Prüfling 42 Frankfurt am Main",
    "phone_number": "+49-69-97696945",
    "websites": [{"url": "http://punjabi-kitchen.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Punjabi-kitchen-Indien-Restaurant/331559740279662", "kind": "facebook"}]
  },
  {
    "name": "Rag Bar",
    "offerings": "options",
    "comment": "Roh-vegan (Untergeschoss Zeilgalerie)",
    "lookup_address": "Zeil 112-114 Frankfurt am Main",
    "phone_number": "+49-176-56589695",
    "websites": [{"url": "http://www.rag-bar.com", "kind": "website"}, {"url": "http://www.facebook.com/pages/Rag-Bar/228126903991643", "kind": "facebook"}]
  },
  {
    "name": "Sachsenhäuser Feinbäckerei",
    "offerings": "options",
    "lookup_address": "Schweizer Straße 44 Frankfurt am Main",
    "phone_number": "+49-69-97694012",
    "websites": [{"url": "http://www.sachsenhaeuser-feinbaeckerei.de", "kind": "website"}, {"url": "https://www.facebook.com/feinbaeckerei", "kind": "facebook"}]
  },
  {
    "name": "Salädchen Bockenheimer Landstraße",
    "offerings": "options",
    "lookup_address": "Bockenheimer Landstraße 43 Frankfurt am Main",
    "phone_number": "+49-69-24449555",
    "websites": [{"url": "http://www.salaedchen.com/laedchen/frankfurt-1.html", "kind": "website"}, {"url": "https://www.facebook.com/SalaedchenFrankfurt1", "kind": "facebook"}]
  },
  {
    "name": "Samasushi",
    "offerings": "options",
    "lookup_address": "Sandweg 62 Frankfurt am Main",
    "phone_number": "+49-69-36602496 ",
    "websites": [{"url": "http://www.samasushi.de", "kind": "website"}, {"url": "https://www.facebook.com/samasushi", "kind": "facebook"}]
  },
  {
    "name": "Sankt Peter Café",
    "offerings": "options",
    "lookup_address": "Bleichstraße 33 Frankfurt am Main",
    "websites": [{"url": "https://www.sanktpeter.com/info/sp-cafe", "kind": "website"}, {"url": "https://www.facebook.com/SanktPeterCafe", "kind": "facebook"}]
  },
  {
    "name": "Sausalitos",
    "offerings": "options",
    "lookup_address": "Kiesstraße 36 Frankfurt am Main",
    "phone_number": "+49-69-70794536",
    "websites": [{"url": "http://www.sausalitos.de/mein-sausalitos/frankfurt.html", "kind": "website"}, {"url": "https://www.facebook.com/Sausalitos.Frankfurt", "kind": "facebook"}]
  },
  {
    "name": "Savanna",
    "offerings": "options",
    "comment": "Ostafrikanisch",
    "lookup_address": "Alte Gasse 69 Frankfurt am Main",
    "phone_number": "+49-69-21998786",
    "websites": [{"url": "http://www.savanna-restaurant.com", "kind": "website"}, {"url": "https://www.facebook.com/pages/Savanna-Restaurant/112629812130038", "kind": "facebook"}]
  },
  {
    "name": "Savory",
    "offerings": "vegan",
    "type": "Bistro-Café",
    "lookup_address": "Burgfriedenstraße 2 Frankfurt am Main",
    "phone_number": "+49-69-74223160",
    "websites": [{"url": "http://www.savory-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/savory.frankfurt", "kind": "facebook"}]
  },
  {
    "name": "Schneider's Café Snackbar Frankfurt",
    "offerings": "options",
    "comment": "(Green-) Smoothies",
    "lookup_address": "Bockenheimer Landstraße 5-7 Frankfurt am Main",
    "phone_number": "+49-69-172389",
    "websites": [{"url": "http://www.schneiders-cafe.de", "kind": "website"}, {"url": "https://www.facebook.com/dieGenussSchneiderei", "kind": "facebook"}]
  },
  {
    "name": "Schuch's Restaurant",
    "offerings": "options",
    "lookup_address": "Alt Praunheim 11 Frankfurt am Main",
    "phone_number": "+49-69-761005",
    "websites": [{"url": "http://www.schuchs-restaurant.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Schuchs-Restaurant/282877415128226", "kind": "facebook"}]
  },
  {
    "name": "Schweiger's Mint",
    "offerings": "options",
    "comment": "Vegane Kuchen und Eis Optionen",
    "lookup_address": "Berger Straße 36 Frankfurt am Main",
    "phone_number": "+49-69-84844211",
    "websites": [{"url": "http://www.schweigers-mint.de", "kind": "website"}, {"url": "https://www.facebook.com/SchweigersMint", "kind": "facebook"}]
  },
  {
    "name": "Seoulfood",
    "offerings": "options",
    "comment": "Koreanisch",
    "lookup_address": "Weserstraße 17 Frankfurt am Main",
    "phone_number": "+49-69-20168645",
    "websites": [{"url": "http://www.seoulfood.eu", "kind": "website"}, {"url": "https://www.facebook.com/seoulfood.eu", "kind": "facebook"}]
  },
  {
    "name": "Special-Ts",
    "offerings": "options",
    "lookup_address": "Oeder Weg 34 Frankfurt am Main",
    "phone_number": "+49-69-27279116",
    "websites": [{"url": "http://www.special-ts.de", "kind": "website"}, {"url": "https://www.facebook.com/specialts.ffm", "kind": "facebook"}]
  },
  {
    "name": "Speisekammer",
    "offerings": "options",
    "lookup_address": "Alt Heddernheim 41 Frankfurt am Main",
    "phone_number": "+49-69-573888",
    "websites": [{"url": "http://www.speisekammer-ffm.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Speisekammer/204427122911896", "kind": "facebook"}]
  },
  {
    "name": "Suppenglück",
    "offerings": "options",
    "lookup_address": "Lyoner Straße 11 Frankfurt am Main",
    "phone_number": "+49-69-66058288",
    "websites": [{"url": "https://www.facebook.com/Suppenglueck", "kind": "facebook"}]
  },
  {
    "name": "Suppengrün",
    "offerings": "options",
    "comment": "mindestens eine vegane Suppe und Salat",
    "lookup_address": "Berger Straße 26 Frankfurt am Main",
    "phone_number": "+49-69-442098",
    "websites": [{"url": "http://www.suppengruen-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Suppengrün/372301159527971", "kind": "facebook"}]
  },
  {
    "name": "Supperia Biringerhof",
    "offerings": "options",
    "comment": "Mindestens eine vegane Suppe",
    "lookup_address": "Albanusstraße 16 Frankfurt am Main",
    "websites": [{"url": "https://www.facebook.com/pages/Supperia-Biringerhof/327843060658678", "kind": "facebook"}]
  },
  {
    "name": "Thai Express Grüneburgweg",
    "offerings": "options",
    "lookup_address": "Grüneburgweg 41-43 Frankfurt am Main",
    "phone_number": "+49-69-71447663",
    "websites": [{"url": "http://www.thai-express.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Thai-Express/152474388126296", "kind": "facebook"}]
  },
  {
    "name": "Thai Express Innenstadt",
    "offerings": "options",
    "lookup_address": "Carl-Theodor-Reiffenstein-Platz 7 Frankfurt am Main",
    "phone_number": "+49-69-232222",
    "websites": [{"url": "http://www.thai-express.de", "kind": "website"}]
  },
  {
    "name": "The Donut People",
    "offerings": "options",
    "lookup_address": "Berger Straße 98 Frankfurt am Main",
    "phone_number": "+40-800-8433668",
    "websites": [{"url": "http://www.thedonutpeople.com", "kind": "website"}, {"url": "http://www.facebook.com/TheDonutPeople", "kind": "facebook"}]
  },
  {
    "name": "Thong Thai",
    "offerings": "options",
    "lookup_address": "Meisengasse 12 Frankfurt am Main",
    "phone_number": "+49-69-92882977",
    "websites": [{"url": "http://www.thong-thai.com", "kind": "website"}, {"url": "https://www.facebook.com/pages/Thong-Thai-Frankfurt/183169691714886", "kind": "facebook"}]
  },
  {
    "name": "Thong Thai",
    "offerings": "options",
    "comment": "Terminal 1A",
    "lookup_address": "Am Flughafen Frankfurt am Main",
    "websites": [{"url": "http://www.thong-thai.com", "kind": "website"}]
  },
  {
    "name": "Tortenengel",
    "offerings": "options",
    "comment": "z.b. Rohkosttörtchen",
    "lookup_address": "Luisenstraße 32 Frankfurt am Main",
    "phone_number": "+49-69-170-3471983",
    "websites": [{"url": "http://www.tortenengel.com", "kind": "website"}, {"url": "https://www.facebook.com/Tortenengel", "kind": "facebook"}]
  },
  {
    "name": "Vapiano Goetheplatz",
    "offerings": "options",
    "lookup_address": "Goetheplatz 1 Frankfurt am Main",
    "phone_number": "+49-6992887888 ",
    "websites": [{"url": "http://de.vapiano.com/de/home", "kind": "website"}]
  },
  {
    "name": "Vapiano Bockenheimer Landstraße",
    "offerings": "options",
    "lookup_address": "Bockenheimer Landstraße 24 Frankfurt am Main",
    "phone_number": "+49-69-71033647",
    "websites": [{"url": "http://de.vapiano.com/de/home", "kind": "website"}]
  },
  {
    "name": "Vapiano Hanauer Landstraße",
    "offerings": "options",
    "lookup_address": "Hanauer Landstraße 148 Frankfurt am Main",
    "phone_number": "+49-69-40565758",
    "websites": [{"url": "http://de.vapiano.com/de/home", "kind": "website"}]
  },
  {
    "name": "Veganz",
    "offerings": "vegan",
    "comment": "Veganer Supermarkt",
    "lookup_address": "Spessartstraße 2 Frankfurt am Main",
    "phone_number": "+49-69-23807792 ",
    "websites": [{"url": "http://www.veganz.de", "kind": "website"}, {"url": "https://www.facebook.com/VeganzWirLiebenLebenFrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Veggie House",
    "offerings": "options",
    "comment": "Lieferservice",
    "lookup_address": "Schlossstraße 125 Frankfurt am Main",
    "phone_number": "+49-69-84843650",
    "websites": [{"url": "http://www.veggiehouse-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/veggiehouse.frankfurt", "kind": "facebook"}]
  },
  {
    "name": "Veinkost",
    "offerings": "vegan",
    "comment": "Veganes Catering",
    "lookup_address": "Gwinner Straße 36 Frankfurt am Main",
    "phone_number": "+49-69-40035480",
    "websites": [{"url": "http://veinkost-ffm.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Ketao/170502372982878", "kind": "facebook"}, {"url": "https://www.facebook.com/pages/Veinkost/364138610368437", "kind": "facebook"}]
  },
  {
    "name": "Vipho",
    "offerings": "options",
    "comment": "Vietnamesisch",
    "lookup_address": "Oeder Weg 21 Frankfurt am Main",
    "phone_number": "+49-69-556746",
    "websites": [{"url": "http://www.vipho.de", "kind": "website"}, {"url": "http://www.facebook.com/vipho.de", "kind": "facebook"}]
  },
  {
    "name": "Vivace Focacceria",
    "offerings": "options",
    "lookup_address": "Gräfstraße 89 Frankfurt am Main",
    "phone_number": "+49-69-84777709",
    "websites": [{"url": "https://www.facebook.com/pages/Vivace-Focacceria/620724798015811", "kind": "facebook"}]
  },
  {
    "name": "Wiesenlust",
    "offerings": "options",
    "comment": "Vegane Burger-Option, alle Saucen, auch Mayo, vegan.",
    "lookup_address": "Berger Straße 77 Frankfurt am Main",
    "phone_number": "+49-69-90436470",
    "websites": [{"url": "http://www.wiesenlust.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Wiesenlust/234487250016562", "kind": "facebook"}]
  },
  {
    "name": "Wondergood",
    "offerings": "vegan",
    "comment": "Veganes Restaurant",
    "lookup_address": "Preungesheimer Straße 1 Frankfurt am Main",
    "phone_number": "+49-69-20162183",
    "websites": [{"url": "http://www.wondergood.de", "kind": "website"}, {"url": "http://www.facebook.com/pages/Wondergood/616747568336454", "kind": "facebook"}]
  },
  {
    "name": "Wondergood Bistro",
    "offerings": "vegan",
    "comment": "Veganes Bistro im Veganz",
    "lookup_address": "Spessartstraße 2 Frankfurt am Main",
    "phone_number": "+49-157-71330996",
    "websites": [{"url": "https://www.facebook.com/WondergoodBistroFrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Yummy Yogurt",
    "offerings": "options",
    "lookup_address": "Berger Straße 77 Frankfurt am Main",
    "phone_number": "+49-69-41072201",
    "websites": [{"url": "http://www.yummy-yogurt.de", "kind": "website"}, {"url": "https://www.facebook.com/yummyyogurtFrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Zaksway Café",
    "offerings": "options",
    "comment": "Segway Verleih",
    "lookup_address": "Sandweg 46 Frankfurt am Main",
    "phone_number": "+49-69-36708592",
    "websites": [{"url": "http://zaksway.de", "kind": "website"}, {"url": "https://www.facebook.com/zaksway", "kind": "facebook"}]
  },
  {
    "name": "Zeit für Brot",
    "offerings": "options",
    "comment": "Bäckerei",
    "lookup_address": "Oeder Weg 15 Frankfurt am Main",
    "phone_number": "+49-69-56998150 ",
    "websites": [{"url": "http://www.zeitfuerbrot.com", "kind": "website"}, {"url": "http://www.facebook.com/zeitfuerbrot", "kind": "facebook"}]
  },
  {
    "name": "Zur Pfeffermühle",
    "offerings": "options",
    "comment": "Betriebsrestaurant der ver.di",
    "lookup_address": "Wilhelm-Leuschner-Straße 69 Frankfurt am Main",
    "websites": [{"url": "http://www.weltdreh.de/gastronomie/zur-pfeffermuehle-kantine-frankfurt-bahnhof", "kind": "website"}]
  },
  {
    "name": "Zur Sonnenuhr",
    "offerings": "options",
    "lookup_address": "Wöllstädter Straße 11 Frankfurt am Main",
    "phone_number": "+49-69-46308977",
    "websites": [{"url": "http://www.zur-sonnenuhr.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Zur-Sonnenuhr/316925611687106", "kind": "facebook"}]
  },
  {
    "name": "Apfelkern und Kolibri",
    "offerings": "options",
    "lookup_address": "Schwedenpfad 6 Bad Homburg",
    "phone_number": "+49-6172-8501360",
    "websites": [{"url": "http://www.apfelkern-und-kolibri.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Café-Bar-Apfelkern-Kolibri/226518684123850", "kind": "facebook"}]
  },
  {
    "name": "Buonissimo",
    "offerings": "options",
    "lookup_address": "Auhofstraße 2 Aschaffenburg",
    "phone_number": "+49-6021-9203394",
    "websites": [{"url": "http://www.bio-buonissimo.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Buonissimo-Italienische-Bio-Erlebnisküche/132242193519823", "kind": "facebook"}]
  },
  {
    "name": "Chili and Beans",
    "offerings": "options",
    "lookup_address": "Kleine Markt Straße 7 Offenbach",
    "phone_number": "+49-171-8181180",
    "websites": [{"url": "http://chiliandbeans.de", "kind": "website"}, {"url": "https://www.facebook.com/chiliandbeans", "kind": "facebook"}]
  },
  {
    "name": "Heidi und Paul",
    "offerings": "options",
    "lookup_address": "Unterortstraße 27 Eschborn",
    "websites": [{"url": "http://www.heidiundpaul.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Heidi-und-Paul/115930075133334", "kind": "facebook"}]
  },
  {
    "name": "La Piazza Toscana",
    "offerings": "options",
    "comment": "Pizzeria",
    "lookup_address": "Rathausplatz 3-7 Bad Homburg",
    "phone_number": "+49-6172-21010",
    "websites": [{"url": "http://www.lapiazzatoscana.de", "kind": "website"}, {"url": "https://www.facebook.com/carpan5860", "kind": "facebook"}]
  },
  {
    "name": "La Morena Gastro-Bar",
    "offerings": "options",
    "lookup_address": "Klosterstraße 12 Königstein im Taunus",
    "phone_number": "+49-6174-1787",
    "websites": [{"url": "http://www.lamorenagastrobar.de", "kind": "website"}, {"url": "https://www.facebook.com/LaMorenaGastroBar", "kind": "facebook"}]
  },
  {
    "name": "Lounge Oberursel",
    "offerings": "options",
    "lookup_address": "Platz der Deutschen Einheit Oberursel",
    "phone_number": "+49-6171-9160171",
    "websites": [{"url": "http://www.lounge-restaurant.de", "kind": "website"}, {"url": "https://www.facebook.com/LOUNGEOberursel", "kind": "facebook"}]
  },
  {
    "name": "Maharaja Palace",
    "offerings": "options",
    "comment": "Indisch",
    "lookup_address": "Königsteiner Straße 47 Bad Soden im Taunus",
    "phone_number": "+49-6196-9698255",
    "websites": [{"url": "http://www.maharaja-palace.de/index_badsoden.html", "kind": "website"}, {"url": "https://www.facebook.com/pages/Maharaja-Palace-Indisches-Restaurant/141323255924402", "kind": "facebook"}]
  },
  {
    "name": "Morleos Bar Restaurant",
    "offerings": "options",
    "lookup_address": "Wilhelmsplatz 14 Offenbach am Main",
    "phone_number": "+49-69-80089689",
    "websites": [{"url": "http://www.morleos.de", "kind": "website"}, {"url": "https://www.facebook.com/MorleosBarRestaurant", "kind": "facebook"}]
  },
  {
    "name": "Rawdies",
    "offerings": "vegan",
    "comment": "(roh) veganes Catering",
    "lookup_address": "Am Jubiläumsstein 24 Rödermark",
    "websites": [{"url": "http://www.rawdies.de", "kind": "website"}, {"url": "https://www.facebook.com/Rawdies", "kind": "facebook"}]
  },
  {
    "name": "Restaurantcafé in der Alten Mühle",
    "offerings": "options",
    "lookup_address": "Lohstraße 13 Bad Vilbel",
    "phone_number": "+49-6101-127283 ",
    "websites": [{"url": "https://www.facebook.com/pages/Restaurantcafé-in-der-ALTEn-MÜHLE/191503510876287", "kind": "facebook"}]
  },
  {
    "name": "Restaurant Kaufmanns",
    "offerings": "options",
    "lookup_address": "Hanauer Lanstraße 31 Gelnhausen",
    "phone_number": "+49-6051-9675000",
    "websites": [{"url": "http://www.restaurant-kaufmanns.de", "kind": "website"}, {"url": "https://www.facebook.com/restaurant.kaufmanns", "kind": "facebook"}]
  },
  {
    "name": "U-Bahn-Stop",
    "offerings": "vegan",
    "comment": "Imbiss",
    "lookup_address": "Frankfurter Landstraße 94 Bad Homburg",
    "phone_number": "+49-6172-8501445",
    "websites": [{"url": "https://www.facebook.com/pages/U-Bahn-Stop/363108823769475", "kind": "facebook"}]
  },
  {
    "name": "Villa Philippe",
    "offerings": "options",
    "lookup_address": "Hainstraße 3 Kronberg",
    "phone_number": "+49-6173-993751",
    "websites": [{"url": "http://www.villa-philippe.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Villa-Philippe-Bar-Restaurant/120093298072073", "kind": "facebook"}]
  },
  {
    "name": "Walgers",
    "offerings": "options",
    "lookup_address": "Wilhelmsplatz 12 Offenbach",
    "phone_number": "+49-69-85093097",
    "websites": [{"url": "http://www.walgers.de", "kind": "website"}, {"url": "https://www.facebook.com/Walgers", "kind": "facebook"}]
  },
  {
    "name": "Tigerpalast",
    "offerings": "options",
    "comment": "2-Sterne Koch",
    "lookup_address": "Heiligkreuzgasse 16-20 Frankfurt am Main",
    "phone_number": "+49-69-9200220",
    "websites": [{"url": "http://www.tigerpalast.de", "kind": "website"}, {"url": "https://www.facebook.com/Tigerpalast", "kind": "facebook"}]
  },
  {
    "name": "Engel - Holzofen Pizza & Pasta",
    "offerings": "options",
    "lookup_address": "Schwalbacher Straße 66 Frankfurt am Main",
    "phone_number": "+49-69-27270066",
    "websites": [{"url": "http://www.gallus-europaviertel.de/gastronomie/italienisch/holzofenpizza-engel.html", "kind": "website"}, {"url": "https://www.facebook.com/pizzapastaengel", "kind": "facebook"}]
  },
  {
    "name": "Strandcafé",
    "offerings": "options",
    "lookup_address": "Koselstraße 46 Frankfurt am Main",
    "phone_number": "+49-69-24145495",
    "websites": [{"url": "http://www.strandcafe-frankfurt.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Strandcafe/189380777837515", "kind": "facebook"}]
  },
  {
    "name": "Coa Terminal 1",
    "offerings": "options",
    "comment": "Flugsteig A, Ebene 2, Atrium",
    "lookup_address": "Flughafen Frankfurt am Main",
    "phone_number": "+49-69-69027545",
    "websites": [{"url": "http://www.coa.as/", "kind": "website"}]
  },
  {
    "name": "Salädchen Frankfurt Flughafen",
    "offerings": "options",
    "comment": "The Squaire - Ebene 3 Fernbahnhof",
    "lookup_address": "Flughafen Frankfurt am Main",
    "phone_number": "+49-69-643552380",
    "websites": [{"url": "http://www.salaedchen.com/laedchen/frankfurt-2.html", "kind": "website"}, {"url": "https://www.facebook.com/SaladchenFrankfurt2", "kind": "facebook"}]
  },
  {
    "name": "Wir essen Blumen",
    "offerings": "vegan",
    "comment": "Roh-vegane Smoothie Bar mit Snacks (alles Bio)",
    "lookup_address": "Sandweg 6c Frankfurt am Main",
    "phone_number": "+49-69-43052616",
    "websites": [{"url": "https://www.facebook.com/BurritoBandeFrankfurt", "kind": "facebook"}]
  },
  {
    "name": "Burrito Bande",
    "offerings": "options",
    "websites": [{"url": "https://www.facebook.com/BurritoBande", "kind": "facebook"}]
  },
  {
    "name": "Gaumenkino",
    "offerings": "vegan",
    "comment": "Veganes Catering, gaumenkino@googlemail.com",
  },
  {
    "name": "Quan Van",
    "offerings": "options",
    "comment": "Vietnamesisch",
    "lookup_address": "Schwarzburgstraße 74 Frankfurt am Main",
    "phone_number": "+49-69-599723",
    "websites": [{"url": "http://www.quanvan.de", "kind": "website"}, {"url": "https://www.facebook.com/pages/Quan-Van/177633912270765", "kind": "facebook"}]
  },
  {
    "name": "Tilos Hotterie",
    "offerings": "options",
    "lookup_address": "Oederweg 39 Frankfurt am Main",
  }
]


url = 'http://localhost:8000/api/restaurants/'
headers = {'content-type': 'application/json'}
user = 'sebastian'
pswd = 'admin'

goal = len(data_dict)
print " "
print "Import of " + str(goal) + " items starting.."
bar_size = 50
bar_start_sym = "["
bar_end_sym = "]"
bar_sym = "|"
bar_fill_sym = " "

for i, data in enumerate(data_dict):
    r = requests.post(url, data=json.dumps(data),
                      auth=(user, pswd), headers=headers)
    """
    print " "
    print " "
    print "NUMBER: " + str(i)
    print " "
    print r.json()
    print " "
    print " "
    """
    progress = int(i/(float(goal)/bar_size)+1)
    sys.stdout.write("\r"+bar_start_sym)
    for j in range(bar_size):
        if j < progress:
            sys.stdout.write(bar_sym)
        else:
            sys.stdout.write(bar_fill_sym)
    rel_progress = float(progress)/float(bar_size)*100
    sys.stdout.write(bar_end_sym+" %d%% " % rel_progress)
    sys.stdout.flush()


"""
print " "
print " "
print "NUMBER: " + str(i)
print " "
print r.json()
print " "
print " "
"""

# payload = {'json_playload': data_json, 'apikey': 'YOUR_API_KEY_HERE'}
# r = requests.post('localhost:8000/api/restaurants/',
# data=payload, auth=('user', 'pass'))
