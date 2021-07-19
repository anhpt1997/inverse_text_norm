python ../OpenNMT-py/train.py -data ../preprocess/data_english  -save_model model/model_itn_purpose -layers 6 -rnn_size 256 -word_vec_size 256 \
-transformer_ff 1024 -heads 8 -encoder_type transformer -decoder_type transformer -position_encoding -train_steps 100000 \
-max_generator_batches 2 -dropout 0.1 -batch_size 1000 -batch_type tokens -normalization tokens -accum_count 2 -optim adam \
-adam_beta2 0.998  -learning_rate 0.001   -save_checkpoint_steps 5000 -world_size 1 -gpu_rank 0  --report_every 100  --log_file train_data_120k
