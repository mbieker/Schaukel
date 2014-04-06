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
        






