
# calcparsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '954EE22A79DC429CE06F75ED53192C33'
    
_lr_action_items = {'RPAREN':([3,11,12,14,15,16,17,18,19,],[-9,19,-10,-7,-5,-6,-4,-3,-8,]),'$end':([1,2,3,5,12,14,15,16,17,18,19,20,],[0,-2,-9,-10,-10,-7,-5,-6,-4,-3,-8,-1,]),'LPAREN':([0,4,6,7,8,9,10,13,],[4,4,4,4,4,4,4,4,]),'TIMES':([2,3,5,11,12,14,15,16,17,18,19,20,],[7,-9,-10,7,-10,-7,-5,-6,7,7,-8,7,]),'PLUS':([2,3,5,11,12,14,15,16,17,18,19,20,],[10,-9,-10,10,-10,-7,-5,-6,-4,-3,-8,10,]),'NUMBER':([0,4,6,7,8,9,10,13,],[3,3,3,3,3,3,3,3,]),'EQUALS':([5,],[13,]),'DIVIDE':([2,3,5,11,12,14,15,16,17,18,19,20,],[8,-9,-10,8,-10,-7,-5,-6,8,8,-8,8,]),'NAME':([0,4,6,7,8,9,10,13,],[5,12,12,12,12,12,12,12,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[6,9,-9,6,-10,6,6,6,6,6,9,-10,6,-7,-5,-6,-4,-3,-8,9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,6,7,8,9,10,13,],[2,11,14,15,16,17,18,20,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','calcparse.py',21),
  ('statement -> expression','statement',1,'p_statement_expr','calcparse.py',25),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','calcparse.py',29),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','calcparse.py',30),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','calcparse.py',31),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','calcparse.py',32),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','calcparse.py',39),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','calcparse.py',43),
  ('expression -> NUMBER','expression',1,'p_expression_number','calcparse.py',47),
  ('expression -> NAME','expression',1,'p_expression_name','calcparse.py',51),
]
