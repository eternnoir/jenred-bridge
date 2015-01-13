#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'eternnoir'
import os
from jenred import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5566))
    app.run('0.0.0.0', port=port)



