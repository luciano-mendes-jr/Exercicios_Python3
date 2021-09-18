#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:31:38 2021

@author: luciano
"""

import pygame 

pygame.init() 
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait() 
