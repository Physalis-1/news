* appps.py - графон(на будущее)
* Датасеты создаюстся с помощью реальных новостей с новстнх сайтов, фейковые новости могут быть созданы следующим образом:
   * Сгенерирован с помощью RUGPT3XL; 
   * Сгенерирован с помощью цепи Маркова на основе текстов реальных новостей с сайтов, код генератора взят(https://github.com/Codecademy/markov_python.git); 
   * Взят отсюда (https://github.com/Tortole/fake_news_detector.git) и помещен в папку fake/ под названием news.csv;     
* Папки:
  * real/  - содержит уже найденые реальные новости; 
  * file_vocab/  - содержит фалы, на основании которых создается словарь; 
  * markov/  - содержит генератор для генерации текста цепями Мароква; 
  * fake/  - содержит новости сгененрированные нейросетью; 
  * vocab/  - содержит словарь; 
* vocab.ipynb - генерирует словарь для отбора новостей с сайтов; 
* create_dataset_real.ipynb - изъятие реальных новостей с сайтов; 
* ruGPT3XL_generation.ipynb - генерирует фейковые новости; 
* internet_dataset_real_fake.ipynb - создает датасет из реальных новостей и фейков из датасета из интернета; 
* fake_real_dataset_gpt3xl.ipynb - создает датасет из реальных новостей и фейков сгенерированных нейросеткой(дочищать приходится руками);  
* MarkovChain_simpl_generator.ipynb - генерирует новости с помощью цепей маркова, создает датасет из реальных нововстей и сгенерированных; 
* bert.ipynb - непосредственно БЕРТ(используется небольшая модель для большей скорости); 


