# Wordnav

This repository contains a collection of files that explore English word embedding systems such as Word2Vec. Alongside the language processing experiments are files pertaining to other areas that interest us, specifically video poker card simulations and a webscraper for nba.com/stats.

## Table Of Contents

- [word_navigator](#word_navigator)
- [nbapi](#nbapi)
- [card](#cards)

## word_navigator
This dude contains some stuff that utilizes the word embeddings downloadable at: [Google News Word Vectors](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g). The file is too large for GitHub, so you will have to download and add to folder yourself.

## nbapi
`nba_api_fun.ipynb` within this folder contains various various code chunks that compile data or create graphs from the NBA stats API. Time-out errors tend to occur with this webscraper if many request are sent to the website in a short period of time, so specific data sets were created and pickled allow quick access. One goal of this project was to crack the [Hoop Grids](https://hoopgrids.com) games, which involves finding every player who played for a certain team or in a certain decade so those datasets were collected.

## cards
Video poker is a single player variant of the game where the player is dealt five cards, then they may select which of the five to keep or replace to build the most winning hand they can. This file contains Numba Just In Time (JIT) optimized code that allows for simulation of millions of hands in the span of seconds. Portions are dedicated to finding the best possible action (out of 32 total actions) for a certain scenario, while others are dedicated to finding the expected return given a machines specific payout table.

<3
---
### Credits

Compound word dataset:
Gagné, C.L., Spalding, T.L. & Schmidtke, D. LADEC: The Large Database of English Compounds. Behav Res 51, 2152–2179 (2019). https://doi.org/10.3758/s13428-019-01282-6