from finmarket_lab.storage.reader import ReaderDataOrderbook

rdo = ReaderDataOrderbook('data/raw/BTCUSDT/orderbook_data.jsonl')
out = rdo.read_all()

print(type(out[0]))
# for key,value in out[0].items():
#     if type(value) is dict:
#         print('__________________')
#         for i,j in value.items():
#             print(type(i),':',type(j))
#         print('_'*10)   
            
#     print(type(key),':',type(value))
#     print(key,':', value)