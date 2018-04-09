from GUIconnect import GUIconnect
from BinaryImage import BinaryImage

class GreyScaleImage(GUIconnect):

    def getThreshold(self, meanIntensity):
        intensity = sum(meanIntensity) // len(meanIntensity)
        return intensity

    def binariseImage(self, data, threshold):
        threshold = int(threshold)
        binaryVals = []
        for i in data:
            x, y, v = i
            x = x.replace(",", "")
            y = y.replace(",", "")
            v = v.replace(",", "")
            if int(v) < threshold:
                v = 0
            elif int(v) >= threshold:
                v = 1
            else:
                pass
            vals = int(x), int(y), int(v)
            binaryVals.append(vals)
        return binaryVals

    def dataForDisplay():
        self.outVals = []
        for i in data:
            x, y, v = i
            x = x.replace(",", "")
            y = y.replace(",", "")
            v = v.replace(",", "")
            vals = int(x), int(y), str(self._determineColorValue(int(v)))
            self.outVals.append(vals)
        return self.outVals

    def _determineColorValue(self,v):
        return ("#%02x%02x%02x" % (v, v, v))
