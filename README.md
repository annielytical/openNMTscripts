Helper scripts for openNMT  
  
preprocessing:  
Obtain dataset (I used WMT Ro-En with parallel files as ro and en)  
Tokenize both dataset files with tokenize_moses.py (edit slightly for each file)  
Split into training and testing with train_val_split.py (edit slightly for each training size)  
  
openNMT commands (1k as example):  
run onmt_build_vocab -config rnn1k.yaml -n_sample 10000000000000 (I just made -n_sample excessively large)  
nmt_train -config rnn1k.yaml  
onmt_translate -model model_step_10000.pt -src src-val1k.txt -output rnn/1k/translations_10000 -gpu -1  
  
evaluation:  
perl multi-bleu.perl tgt-val1k.txt < rnn/1k/translations_10000  
