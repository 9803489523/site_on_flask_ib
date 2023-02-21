
import xml.etree.ElementTree as ET

class Card:
    def __init__(self, header, hrefs):
        self.header = header
        self.hrefs = hrefs
    def printCard(self):
        counter = 0
        print(self.header)
        for h in self.hrefs:
            print(f'[source]: {self.hrefs[counter]["source"]} [href]: {self.hrefs[counter]["href"]}')
            counter +=1

    def __init__(self):
        self.header = ""
        self.hrefs = []

    def fillInByXML(self, direct, filename):
        tree = ET.parse(f"resources/{direct}/{filename}.xml")
        root = tree.getroot()
        self.header = root[0].text
        counter = 0
        for i in root:
            for j in i:
                self.hrefs.append({'source': j[0].text, 'href': j[1].text})
                counter = counter + 1

kiCards = []
bsCards = []
pdCards = []
grCards = []
sCards = []
gdCards = []
gamCards = []
tcCards = []
odCards = []

def fillInKII():
    card1 = Card()
    card1.fillInByXML("kii", "Base documents")
    card2 = Card()
    card2.fillInByXML("kii", "Connection")
    card3 = Card()
    card3.fillInByXML("kii", "Tack")
    card4 = Card()
    card4.fillInByXML("kii", "Gossopka")

    kiCards.append(card1)
    kiCards.append(card2)
    kiCards.append(card3)
    kiCards.append(card4)

def fillInBankSecurity():
    card1 = Card()
    card1.fillInByXML("bankSecurity", "BankStandarts")
    card2 = Card()
    card2.fillInByXML("bankSecurity", "Crypto")
    card3 = Card()
    card3.fillInByXML("bankSecurity", "SecurityGOSTS")
    card4 = Card()
    card4.fillInByXML("bankSecurity", "BankActs")

    bsCards.append(card1)
    bsCards.append(card2)
    bsCards.append(card3)
    bsCards.append(card4)

def fillInPersonalData():
    card1 = Card()
    card1.fillInByXML("personalData", "BaseDocuments")
    card2 = Card()
    card2.fillInByXML("personalData", "Security")
    card3 = Card()
    card3.fillInByXML("personalData", "ViolaterBlock")
    card4 = Card()
    card4.fillInByXML("personalData", "BankSpecific")
    card5 = Card()
    card5.fillInByXML("personalData", "BiometricSystem")
    card6 = Card()
    card6.fillInByXML("personalData", "DataProcessing")
    card7 = Card()
    card7.fillInByXML("personalData", "StoragePeriod")
    card8 = Card()
    card8.fillInByXML("personalData", "InternationalRequirements")
    card9 = Card()
    card9.fillInByXML("personalData", "InternalDocs")

    pdCards.append(card1)
    pdCards.append(card2)
    pdCards.append(card3)
    pdCards.append(card4)
    pdCards.append(card5)
    pdCards.append(card6)
    pdCards.append(card7)
    pdCards.append(card8)
    pdCards.append(card9)

def fillInGovRegulation():
    card2 = Card()
    card2.fillInByXML("govRegulation", "FSB")
    card1 = Card()
    card1.fillInByXML("govRegulation", "FSTEK")
    card3 = Card()
    card3.fillInByXML("govRegulation", "MinComsvyaz")
    card4 = Card()
    card4.fillInByXML("govRegulation", "Roscomnadzor")
    card5 = Card()
    card5.fillInByXML("govRegulation", "RussianBank")
    card6 = Card()
    card6.fillInByXML("govRegulation", "MinOborony")
    card7 = Card()
    card7.fillInByXML("govRegulation", "MinYust")
    card8 = Card()
    card8.fillInByXML("govRegulation", "MID")

    grCards.append(card1)
    grCards.append(card2)
    grCards.append(card3)
    grCards.append(card4)
    grCards.append(card5)
    grCards.append(card6)
    grCards.append(card7)
    grCards.append(card8)

def fillInSecret():
    card1 = Card()
    card1.fillInByXML("secret", "Government")
    card2 = Card()
    card2.fillInByXML("secret", "Commercial")
    card3 = Card()
    card3.fillInByXML("secret", "Official")
    card4 = Card()
    card4.fillInByXML("secret", "Bank")
    card5 = Card()
    card5.fillInByXML("secret", "Insider")

    sCards.append(card1)
    sCards.append(card2)
    sCards.append(card3)
    sCards.append(card4)
    sCards.append(card5)

def fillInGeneralDocs():
    card3 = Card()
    card3.fillInByXML("generalDocs", "LawBase")
    card2 = Card()
    card2.fillInByXML("generalDocs", "System")
    card1 = Card()
    card1.fillInByXML("generalDocs", "Strategy")

    gdCards.append(card1)
    gdCards.append(card2)
    gdCards.append(card3)

def fillInGISandMIS():
    card1 = Card()
    card1.fillInByXML("GISandMIS", "BaseDocuments")
    card2 = Card()
    card2.fillInByXML("GISandMIS", "SMEW")
    card3 = Card()
    card3.fillInByXML("GISandMIS", "Security")
    card4 = Card()
    card4.fillInByXML("GISandMIS", "Data")
    card5 = Card()
    card5.fillInByXML("GISandMIS", "Medicine")

    gamCards.append(card1)
    gamCards.append(card2)
    gamCards.append(card3)
    gamCards.append(card4)
    gamCards.append(card5)

def fillInTechnicalControl():
    card1 = Card()
    card1.fillInByXML("technicalControl", "BaseDocuments")
    card2 = Card()
    card2.fillInByXML("technicalControl", "Specification")
    card3 = Card()
    card3.fillInByXML("technicalControl", "Attestation")

    tcCards.append(card1)
    tcCards.append(card2)
    tcCards.append(card3)

def fillInOtherDocs():
    card1 = Card()
    card1.fillInByXML("otherDocs", "SecurityCommunication")
    card2 = Card()
    card2.fillInByXML("otherDocs", "SecurityAndPersonal")
    card3 = Card()
    card3.fillInByXML("otherDocs", "Litigation")
    card4 = Card()
    card4.fillInByXML("otherDocs", "Cryptography")
    card5 = Card()
    card5.fillInByXML("otherDocs", "Signature")
    card6 = Card()
    card6.fillInByXML("otherDocs", "Transport")
    card7 = Card()
    card7.fillInByXML("otherDocs", "Payments")
    card8 = Card()
    card8.fillInByXML("otherDocs", "Medicine")
    card9 = Card()
    card9.fillInByXML("otherDocs", "Education")
    card10 = Card()
    card10.fillInByXML("otherDocs", "Inoagents")

    odCards.append(card1)
    odCards.append(card2)
    odCards.append(card3)
    odCards.append(card4)
    odCards.append(card5)
    odCards.append(card6)
    odCards.append(card7)
    odCards.append(card8)
    odCards.append(card9)
    odCards.append(card10)