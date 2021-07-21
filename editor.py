#!/usr/bin/env python
# -*- coding: utf-8 -*

import global_var
import modules.map.proto as proto

import matplotlib.pyplot as plt

# Elements with changed attributes
changed_artist = []

def clear_properties():
  for artist in changed_artist:
    artist.set_color('g')
    artist.set_label('')

def set_properties(obj, color, label):
  obj.set_color(color)
  obj.set_label(label)

def show_lane_detail(line, lane):
  set_properties(line, 'red', "cur_lane: " + lane.id.id)
  changed_artist.append(line)
  # pre lanes
  for predecessor_id in lane.predecessor_id:
    line = global_var.get_element_value(predecessor_id.id)
    if line:
      set_properties(line, 'cyan', "pre_lane: " + predecessor_id.id)
      changed_artist.append(line)
  # successor lanes
  for successor_id in lane.successor_id:
    line = global_var.get_element_value(successor_id.id)
    if line:
      set_properties(line, 'purple', "suc_lane: " + successor_id.id)
      changed_artist.append(line)

  # lane.left_neighbor_forward_lane_id
  # lane.right_neighbor_forward_lane_id
  # lane.left_neighbor_reverse_lane_id
  # lane.right_neighbor_reverse_lane_id

def on_click(event):
  pass

def on_pick(event):
  # 1. clear preview label first
  clear_properties()

  # 2. find event.artist 
  obj = global_var.get_artist_value(event.artist)
  # print(event.artist)  
  if isinstance(obj, proto.map_lane_pb2.Lane):
    show_lane_detail(event.artist, obj)
  
  # 3. redraw
  plt.legend()
  plt.draw()

def on_press(event):
  pass

def on_release(event):
  pass

def on_motion(event):
  pass
