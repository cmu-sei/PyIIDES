"""
License:
PyIIDES
Copyright 2024 Carnegie Mellon University.
NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS. CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
Licensed under a MIT (SEI)-style license, please see license.txt or contact permission@sei.cmu.edu for full terms.
[DISTRIBUTION STATEMENT A] This material has been approved for public release and unlimited distribution.  Please see Copyright notice for non-US Government use and distribution.
DM24-1597
"""
from pyiides.pyiides import *
from datetime import date, datetime, timedelta 

def basic_tests() -> bool:
    print("Testing Basic Functionality...")
    i = Incident()

    assert(i.id != None)
    assert(isinstance(i.id, str))

    print(f"-> The id for an Incident example is {i.id}")

    i1 = Incident(cia_effect = ['C'])
    assert(i1.cia_effect == ['C'])

    exampledate =  datetime.fromisoformat('2021-02-02')
    t = TTP(date = exampledate)

    assert(isinstance(t.id, str))
    assert(t.date == exampledate)

    ins = Insider(first_name='Amanda', incident_role='1')
    assert(ins.first_name == 'Amanda')

    try:
        job = Job(hire_date = '1234')
    except:
        print("-> Correctly did not allow poorly formatted hire date for Job initialization")
    
    d = Detection()

    try:
        d.first_detected = 'hello there'
    except:
        print("-> Correctly did not allow poorly formatted first_detected date for Detection class")

    print("Passed Basic Functionality Tests\n\n")
    return True


def incident_tests() -> bool:
    print("Testing Incident Class Functionality...")
    i = Incident(cia_effect = ['C'])
    i.cia_effect.append('I')

    assert(i.cia_effect == ['C', 'I'])
    i.cia_effect.clear() 
    assert(i.cia_effect == [])

    print("Passed Incident Class Functionality Tests\n\n")
    return True


def relationship_tests() -> bool:
    print("Testing Relationship Functionality between Classes...")

    i = Incident()
    t = TTP()

    i.ttps = [t]
    assert(i.ttps == [t])
    assert(t.incident == i)

    o1 = Organization()
    o2 = Organization()

    i.organizations = [o1, o2]
    assert(i.organizations == [o1, o2])
    assert(o1.incident == i)
    assert(o2.incident == i)

    j1 = Job()
    j2 = Job()

    o1.jobs = [j1, j2]
    assert(o1.jobs == [j1, j2])
    assert(j1.organization == o1)
    assert(j2.organization == o1)
    assert(j1.organization.incident == i)

    ins = Insider(incident_role = "1")

    ins.jobs = [j1, j2]
    assert(ins.jobs == [j1, j2])
    assert(j1.insider == ins)

    print("Passed Relationship Functionality between Classes\n\n")
    return True


def vocab_tests() -> bool:
    print("Testing Vocab Check Functionality...")

    # Country Vocab:
    try: 
        p = Person(country = 'ZZ')
    except: 
        print("-> Correctly did not allow poorly formatted Person country")

    p = Person(country = 'US')
    try:
        p.country("Pakistan")
    except:
        print("-> Correctly did not allow poorly formatted Person country reset")
    
    # Detection Vocab
    try: 
        d = Detection(detected_method = ['6'])
    except: 
        print("-> Correctly did not allow poorly formatted Detection method")
    
    try: 
        d = Detection(detected_method = ['1', '2', '3'])
    except: 
        print("-> Incorrectly did not allow properly formatted Detection method")
        return False

    assert(d.detected_method == ['1', '2', '3'])

    d.detected_method = ['1', '5']

    try:
        d.pyiides_append("6")
        return False
    except: 
        print("-> Correctly did not allow poorly formatted Detection method append")

    # -------------------- #
    #       Incident       #
    # -------------------- #
    i = Incident()
    try: 
        i.cia_effect = ["C", "A", "K"]
    except:
        print("-> Correctly did not allow poorly formatted CIA effect")
    i.cia_effect = ["C", "I", "A"]
    assert(i.cia_effect == ["C", "I", "A"])
  
    try: 
        i.incident_type = ["F", "S"]
    except TypeError:
        print("-> Correctly did not allow poorly formatted incident type")
    
    i.incident_type = ["F", "S", "V"]
    assert(i.incident_type == ["F", "S", "V"])

    ## LOOKS LIKE THE SAME SETTER IS BEING USED FOR SUBTYPE AND TYPE, do they all need seperate names?
    ## THIS IS AN ISSUE...ter
    # try: 
    #     i.incident_subtype = ["F.1", "F.2", "Z.2"]
    # except TypeError:
    #     print("-> Correctly did not allow poorly formatted incident type")
    # i.incident_subtype = ["F1", "F2"]
    # assert(i.incident_subtype == ["F1", "F2"])
    
    print("Passed Vocab Check Functionality\n\n")
    return True


def main():
    print("Beginning Tests: \n")

    assert(basic_tests())
    assert(incident_tests())
    assert(relationship_tests())
    assert(vocab_tests())

    print("Passed all Tests!! Hip hip hooray!\n")

if __name__ == "__main__":
    main()