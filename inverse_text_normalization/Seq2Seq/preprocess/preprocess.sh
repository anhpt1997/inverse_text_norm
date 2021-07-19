python ../OpenNMT-py/preprocess.py -train_src ../../data_process/src_oov_1m.txt \
-train_tgt ../../data_process/tgt_oov_1m.txt -save_data data_english \
--shard_size 1000000 --overwrite --src_seq_length 512 --tgt_seq_length 512 \
--src_words_min_frequency 1 --tgt_words_min_frequency 1 --src_vocab_size 200000 --tgt_vocab_size 200000
