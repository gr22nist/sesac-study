from gnrts.common_gnrt import IdGRNT
from gnrts.common_gnrt import AddressGNRT
from gnrts.store_gnrt import STR_NameGNRT
from gnrts.store_gnrt import STR_TypeGNRT

class STR_DataGNRT:
    def __init__(self, num):
        self.num = num
        self.id_gen = IdGRNT()
        self.name_gen = STR_NameGNRT()
        self.type_gen = STR_TypeGNRT()
        self.add_gen = AddressGNRT()
        
    
    def gnrt_stores(self):
        self.data = []
        for _ in range(self.num):
            strid = self.id_gen.gnrt_id()
            strtype = self.name_gen.gnrt_store()
            name = f"{strtype} {self.name_gen.gnrt_store()}"
            address = self.type_gen.gnrt_type()
        
            self.data.append((strid, name, strtype, address)) 
            
        return self.data