import argparse
import sys


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser()

    # Data loading params
    # parser.add_argument("--train_path", default="SemEval2010_task8_all_data/SemEval2010_task8_training/TRAIN_FILE.TXT",
    #                     type=str, help="Path of train data")
    # parser.add_argument("--test_path", default="SemEval2010_task8_all_data/SemEval2010_task8_testing_keys/TEST_FILE_FULL.TXT",
    #                     type=str, help="Path of test data")
    parser.add_argument("--train_path", default="myData/train.txt",
                        type=str, help="Path of train data")
    parser.add_argument("--test_path",
                        default="myData/test.txt",
                        type=str, help="Path of test data")
    parser.add_argument("--max_sentence_length", default=202,
                        type=int, help="Max sentence length in data")
    parser.add_argument("--dev_sample_percentage", default=0.1,
                        type=float, help="Percentage of the training data to use for validation")
    parser.add_argument("--relation_file", default="myData/relation2id.txt",
                        type=str, help="Path of relation file")

    # Model Hyper-parameters
    # Embeddings
    parser.add_argument("--embedding_path", default=None,
                        type=str, help="Path of pre-trained word embeddings (word2vec)")
    parser.add_argument("--text_embedding_dim", default=100,
                        type=int, help="Dimensionality of word embedding (default: 300)")
    parser.add_argument("--pos_embedding_dim", default=50,
                        type=int, help="Dimensionality of relative position embedding (default: 50)")
    # CNN
    parser.add_argument("--filter_sizes", default="2,3,4,5",
                        type=str, help="Comma-separated filter sizes (Default: 2,3,4,5)")
    parser.add_argument("--num_filters", default=128,
                        type=int, help="Number of filters per filter size (Default: 128)")

    # Misc
    parser.add_argument("--desc", default="",
                        type=str, help="Description for model")
    parser.add_argument("--dropout_keep_prob", default=0.5,
                        type=float, help="Dropout keep probability of output layer (default: 0.5)")
    parser.add_argument("--l2_reg_lambda", default=1e-5,
                        type=float, help="L2 regularization lambda (default: 1e-5)")

    # Training parameters
    parser.add_argument("--batch_size", default=20,
                        type=int, help="Batch Size (default: 20)")
    parser.add_argument("--num_epochs", default=100,
                        type=int, help="Number of training epochs (Default: 100)")
    parser.add_argument("--display_every", default=10,
                        type=int, help="Number of iterations to display training information")
    parser.add_argument("--evaluate_every", default=100,
                        type=int, help="Evaluate model on dev set after this many steps (default: 100)")
    parser.add_argument("--num_checkpoints", default=5,
                        type=int, help="Number of checkpoints to store (default: 5)")
    parser.add_argument("--learning_rate", default=1.0,
                        type=float, help="Which learning rate to start with (Default: 1.0)")
    parser.add_argument("--decay_rate", default=0.9,
                        type=float, help="Decay rate for learning rate (Default: 0.9)")

    # Testing parameters
    parser.add_argument("--checkpoint_dir", default="runs/1565578114/checkpoints",
                        type=str, help="Checkpoint directory from training run")

    # Misc Parameters
    parser.add_argument("--allow_soft_placement", default=True,
                        type=bool, help="Allow device soft device placement")
    parser.add_argument("--log_device_placement", default=False,
                        type=bool, help="Log placement of ops on devices")
    parser.add_argument("--gpu_allow_growth", default=True,
                        type=bool, help="Allow gpu memory growth")

    # Log
    parser.add_argument("--train_log_file", default="train.log", type=str, help="name for train log")
    parser.add_argument("--test_log_file", default="test.log", type=str, help="name for test log")

    if len(sys.argv) == 0:
        parser.print_help()
        sys.exit(1)

    print("")
    args = parser.parse_args()
    for arg in vars(args):
        print("{}={}".format(arg.upper(), getattr(args, arg)))
    print("")

    return args


FLAGS = parse_args()
