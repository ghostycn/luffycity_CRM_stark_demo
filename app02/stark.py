#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from stark.service.v1 import site,StarkHander
from app02 import models

site.register(models.Host)

site.register(models.Role)
