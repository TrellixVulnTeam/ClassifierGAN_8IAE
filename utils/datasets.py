# Copyright 2019 Lorna Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Intelligent simplify code volume, easy to load data"""

import torch.utils.data
import torchvision.transforms as transforms

import datasets


def load_datasets(name, root, batch_size):
  if name == "mnist":
    train_dataset = datasets.MNIST(root=root,
                                   download=True,
                                   train=True,
                                   transform=transforms.Compose([
                                     transforms.Resize(28),
                                     transforms.RandomHorizontalFlip(),
                                     transforms.ToTensor(),
                                     transforms.Normalize([0.5], [0.5]),
                                   ]))

    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size,
                                                   shuffle=True, num_workers=8)
    test_dataset = datasets.MNIST(root=root,
                                  download=True,
                                  train=False,
                                  transform=transforms.Compose([
                                    transforms.Resize(28),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.5], [0.5]),
                                  ]))

    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size,
                                                  shuffle=False, num_workers=8)
    return train_dataloader, test_dataloader

  elif name == "fmnist":
    train_dataset = datasets.FashionMNIST(root=root,
                                          download=True,
                                          train=True,
                                          transform=transforms.Compose([
                                            transforms.Resize(28),
                                            transforms.RandomHorizontalFlip(),
                                            transforms.ToTensor(),
                                            transforms.Normalize([0.5], [0.5]),
                                          ]))

    train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=128,
                                                   shuffle=True, num_workers=8)
    test_dataset = datasets.FashionMNIST(root=root,
                                         download=True,
                                         train=False,
                                         transform=transforms.Compose([
                                           transforms.Resize(28),
                                           transforms.ToTensor(),
                                           transforms.Normalize([0.5], [0.5]),
                                         ]))

    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=128,
                                                  shuffle=False, num_workers=8)
    return train_dataloader, test_dataloader
