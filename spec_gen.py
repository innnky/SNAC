from data_utils import TextAudioSpeakerLoader
import json
from tqdm import tqdm

from utils import HParams

config_path = 'configs/config.json'
with open(config_path, "r") as f:
    data = f.read()
config = json.loads(data)
hps = HParams(**config)

train_dataset = TextAudioSpeakerLoader(hps.data.training_files, hps.data)
eval_dataset = TextAudioSpeakerLoader(hps.data.validation_files, hps.data)

for _ in tqdm(train_dataset):
    pass
for _ in tqdm(eval_dataset):
    pass