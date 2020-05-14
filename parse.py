import re

class Parse:
    def __init__(self, data):

        self.data = data
        self.result = {}

    def getVTPDomain(self):
        pattern = re.compile('VTP Domain Name')
        vtpDomain = ''

        for elem in self.data:   
            match = pattern.search(elem)
            
            if match:
                vtpDomain = elem.split(':')[-1].strip()
                break
            
        if vtpDomain:
            self.result['vtpDomain'] = vtpDomain
        else:
            
            self.result['vtpDomain'] = 'Not Set'
        print(self.result.get('vtpDomain'))
        return self.result
    
    def getVTPOperationMode(self):
        pattern = re.compile('VTP Operating Mode')
                
        vtpOpMode = ''

        for elem in self.data:   
            match = pattern.search(elem)
            
            if match:
                vtpOpMode = elem.split(':')[-1].strip()
                break
            
        if vtpOpMode:
            self.result['vtpOpMode'] = vtpOpMode
        else:
            self.result['vtpOpMode'] = 'Unknown'
        print(self.result.get('vtpOpMode'))
        return self.result
                
                