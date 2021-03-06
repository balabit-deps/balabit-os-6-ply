
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '0B7CA54BA0A88793C5105FA7D7A311EB'
    
_lr_action_items = {'RPAREN':([2,4,10,11,12,13,14,15,16,],[-9,-10,16,-7,-3,-4,-2,-1,-8,]),'PLUS':([1,2,4,10,11,12,13,14,15,16,],[9,-9,-10,9,-7,-3,-4,-2,-1,-8,]),'LPAREN':([0,3,5,6,7,8,9,],[3,3,3,3,3,3,3,]),'TIMES':([1,2,4,10,11,12,13,14,15,16,],[6,-9,-10,6,-7,-3,-4,6,6,-8,]),'$end':([1,2,4,11,12,13,14,15,16,],[0,-9,-10,-7,-3,-4,-2,-1,-8,]),'NUMBER':([0,3,5,6,7,8,9,],[2,2,2,2,2,2,2,]),'DIVIDE':([1,2,4,10,11,12,13,14,15,16,],[7,-9,-10,7,-7,-3,-4,7,7,-8,]),'NAME':([0,3,5,6,7,8,9,],[4,4,4,4,4,4,4,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,],[5,8,-9,5,-10,5,5,5,5,5,8,-7,-3,-4,-2,-1,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,5,6,7,8,9,],[1,10,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','expression.py',4),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','expression.py',5),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','expression.py',6),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','expression.py',7),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','statement.py',4),
  ('statement -> expression','statement',1,'p_statement_expr','statement.py',8),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','expression.py',14),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','expression.py',18),
  ('expression -> NUMBER','expression',1,'p_expression_number','expression.py',22),
  ('expression -> NAME','expression',1,'p_expression_name','expression.py',26),
]
