from mongodb.connection import collection
from config.settings import logger
from config.settings import args
from config.classes import Converting, ClientMongoDB




converter  = Converting()
database   = ClientMongoDB(converter, collection)



if __name__ == '__main__':
    logger.info('Start mongodb_client.py')
    
    filter, output_format, output_limit, output_size = database.get_filter(args)

    if output_limit == 'one':
        database.show_record(filter, output_format)
    else:
        database.show_all_records(filter, output_format, output_limit, output_size)





'''
  Title                      Юбка                                                                
  SKU                        FN-WN-SKIR000099                                                    
  Color                      Персиковый                                                          
  Brand                      Acne Studios                                                        
  Gender                     Ж                                                                   
  Material                   100% Полиэстер                                                      
  Fashion Season             2019-2                                                              
  Fashion Collection         Acne Studios Donna FW 2019                                          
  Fashion Collection Inner   Acne Studios Womens RTW Main                                        
  Country                    КИТАЙ                                                               
  Category                   Юбка                                                                
  Price                      11990 RUB                                                           
  Discount                   8990 RUB                                                            
  Sale                       True                                                                
  Leftovers                  ♦ Size: 36, Count: 1, Price: 8990 RUB                               
  Leftovers                  ♦ Size: 38, Count: 1, Price: 8990 RUB                               
  URL Link:                  https://ppassage.com/women/catalog/?search=FN-WN-SKIR000099&page=1  
'''



