'''
Hier werden Funktionen zum Speichern der Messungen und zum Exportieren der Messudaten
als CSV usw.
'''
# Export der Messdaten als CSV im Format |||||||

from PyQt4.Qt import QVector2D


def ExportCSV(RecTmp, Filename, Seperator = ',', NoneChar = None):
    import csv
    from PyQt4.Qt import QVector2D
    
    with open(Filename, 'wb') as f:
        writer = csv.writer(f, delimiter= Seperator)
        for Record in RecTmp:
            Row = []
            for Point in Record:
                if Point == None:
                    Row.extend([NoneChar,NoneChar])
                else:
                    Row.append(Point.x())
                    Row.append(Point.y())
            writer.writerow(Row)
        return True
        

### Messung im eigenen Format speicheren

def SaveData(RecTmp, JointList, ReferencePoint, Filename):
    import pickle , hashlib
    with open(Filename, 'wb') as savefile:
        
        data = pickle.dumps([RecTmp,JointList,ReferencePoint])
        savefile.write(hashlib.md5(data+"Daleks").hexdigest()+'\n'+data)
        savefile.close()
        return True
    return False
        
        

def LoadData(Filename):

    import pickle, hashlib
    with open(Filename, 'rb') as loadfile:
        content = loadfile.read()
        data = content[33:]
        checksum = hashlib.md5(data+"Daleks").hexdigest()
        print checksum
        print content[:32]
        if checksum == content[:32]:
            print "gut"
            return True , pickle.loads(data)
        else:
            return False,( None, None, None)
    return False, (None , None ,None)



