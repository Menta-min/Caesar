import unittest
from Shifr import encryptionCaesar
from Shifr import decryptionCaesar
class TestShifr(unittest.TestCase):
    def test_encryptionCaesar(self):
        self.assertEqual(encryptionCaesar('abc',2),'cde')
        self.assertEqual(encryptionCaesar('Zakirova',6),'Fgqoxubg')
        self.assertEqual(encryptionCaesar('On weekends, I often meet my friends or stay at home and read books.',7),'Vu dllrlukz, P vmalu tlla tf myplukz vy zahf ha ovtl huk ylhk ivvrz.')
        self.assertEqual(encryptionCaesar('Literature, cooking, TV, I have a lot of topics to talk about and make new friends.',25),'Khsdqzstqd, bnnjhmf, SU, H gzud z kns ne snohbr sn szkj zants zmc lzjd mdv eqhdmcr.')
        self.assertEqual(encryptionCaesar('Diana',0),'Diana')
    
    def test_decryptionCaesar(self):
        self.assertEqual(decryptionCaesar('cde',2),'abc') 
        self.assertEqual(decryptionCaesar('Fgqoxubg',6),'Zakirova')
        self.assertEqual(decryptionCaesar('Vu dllrlukz, P vmalu tlla tf myplukz vy zahf ha ovtl huk ylhk ivvrz.',7),'On weekends, I often meet my friends or stay at home and read books.')
        self.assertEqual(decryptionCaesar('Khsdqzstqd, bnnjhmf, SU, H gzud z kns ne snohbr sn szkj zants zmc lzjd mdv eqhdmcr.',25),'Literature, cooking, TV, I have a lot of topics to talk about and make new friends.')
        self.assertEqual(decryptionCaesar('Diana',0),'Diana')     
        
if __name__ =='__main__':
    unittest.main()