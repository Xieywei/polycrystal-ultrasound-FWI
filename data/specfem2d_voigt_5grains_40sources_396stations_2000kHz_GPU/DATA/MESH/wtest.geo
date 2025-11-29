Point (1) = {0.004000000000,-0.004000000000,0.000000000000}; 
Point (2) = {0.004000000000,-0.001108595522,-0.000000000000}; 
Point (3) = {-0.000310954495,-0.004000000000,-0.000000000000}; 
Point (4) = {0.000085597601,-0.001531020115,-0.000000000000}; 
Point (5) = {0.004000000000,0.001108590281,-0.000000000000}; 
Point (6) = {-0.000729202323,0.000000019794,0.000000000000}; 
Point (7) = {0.000085636177,0.001531021202,-0.000000000000}; 
Point (8) = {-0.004000000000,0.004000000000,0.000000000000}; 
Point (9) = {-0.004000000000,-0.000000012681,-0.000000000000}; 
Point (10) = {-0.000310992209,0.004000000000,-0.000000000000}; 
Point (11) = {-0.004000000000,-0.004000000000,0.000000000000}; 
Point (12) = {0.004000000000,0.004000000000,0.000000000000}; 
Point (13) = {-0.004000000000, 0.0015, 0};
Point (14) = {0.004000000000, 0.0, 0};
Point (15) = {-0.004000000000, -0.0015, 0};
Line (1) = {1,2}; 
Line (2) = {3,1}; 
Line (3) = {3,4}; 
Line (4) = {4,2}; 
//Line (5) = {2,5}; 
Line (6) = {4,6}; 
Line (7) = {6,7}; 
Line (8) = {7,5}; 
//Line (9) = {8,9}; 
Line (10) = {10,8}; 
Line (11) = {10,7}; 
Line (12) = {6,9}; 
//Line (13) = {9,11}; 
Line (14) = {11,3}; 
Line (15) = {5,12}; 
Line (16) = {12,10}; 

Line (17) = {4, 15};
Line (18) = {6, 14};
Line (19) = {7, 13};
Line (20) = {15,11};
Line (21) = {15,9};
Line (22) = {14,2};
Line (23) = {14, 5};
Line (24) = {13, 9};
Line (25) = {13, 8};

Line Loop (1) = {-1,-2,3,4};
Plane Surface (1) = {-1}; 

Line Loop (2) = {-4,6,18,22};
Line Loop (3) = {-18,7,8,-23};
Plane Surface (2) = {-2}; 
Plane Surface (3) = {-3};

Line Loop (4) = {-7,12,-24,-19};
Line Loop (5) = {19,25,-10,11};
Plane Surface (4) = {-4}; 
Plane Surface (5) = {-5};

Line Loop (6) = {-14,-20,-17,-3};
Line Loop (7) = {17,21,-12,-6};
Plane Surface (6) = {-6};
Plane Surface (7) = {-7}; 

Line Loop (8) = {-15,-8,-11,-16};
Plane Surface (8) = {-8}; 

Physical Surface ("M11") = {1};
Physical Surface ("M12") = {2,3};
Physical Surface ("M13") = {4,5};
Physical Surface ("M14") = {6,7};
Physical Surface ("M15") = {8};

//Physical Curve("Top") = {10,16};
//Physical Curve("Bottom") = {2,14};
//Physical Curve("Left") = {20,21,24,25};
//Physical Curve("Right") = {1,22,23,15};


//+
Recombine Surface {:};

// meshing
// quads mesh
//Mesh.SubdivisionAlgorithm = 1;
Mesh.ElementOrder = 1;
Mesh.CharacteristicLengthFactor = 0.4;

Point(16) = {-0.005, 0.005, 0, 0.0001};
Point(17) = {0.005, 0.005, 0, 0.0001};
Point(18) = {-0.005, -0.005, 0, 0.0001};
Point(19) = {0.005, -0.005, 0, 0.0001};
Point(20) = {-0.004, 0.005, 0, 0.0001};
Point(21) = {0.004, 0.005, 0, 0.0001};
Point(22) = {0.005, 0.004, 0, 0.0001};
Point(23) = {0.005, -0.004, 0, 0.0001};
Point(24) = {0.004, -0.005, 0, 0.0001};
Point(25) = {-0.004, -0.005, 0, 0.0001};
Point(26) = {-0.005, -0.004, 0, 0.0001};
Point(27) = {-0.005, 0.004, 0, 0.0001};
Line(26) = {20, 21};
Line(27) = {22, 23};
Line(28) = {24, 25};
Line(29) = {26, 27};
Line(30) = {27, 16};
Line(31) = {16, 20};
Line(32) = {20, 8};
Line(33) = {8, 27};
Line(34) = {21, 17};
Line(35) = {17, 22};
Line(36) = {22, 12};
Line(37) = {12, 21};
Line(38) = {23, 19};
Line(39) = {19, 24};
Line(40) = {24, 1};
Line(41) = {1, 23};
Line(42) = {25, 18};
Line(43) = {18, 26};
Line(44) = {26, 11};
Line(45) = {11, 25};

Transfinite Curve {16} = 19;
Transfinite Curve {2} = 19;
Transfinite Curve {4,8} = 19;
Transfinite Curve {-15, -1} = 12;
Transfinite Curve {3,11} = 12;
Transfinite Curve {14} = 18;
Transfinite Curve {10} = 18;
//Transfinite Curve {5} = 7;
//Transfinite Curve {-13, -9} = 11;

Transfinite Curve {12} = 18;
Transfinite Curve {6,7} = 8;

Transfinite Curve {17,19} = 18;
Transfinite Curve {18} = 19;
Transfinite Curve {20,25} = 12;
Transfinite Curve {21,24} = 8;
Transfinite Curve {22,23} = 8;

Transfinite Curve {30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45} = 5;
Transfinite Curve {26} = 36;
Transfinite Curve {27} = 37;
Transfinite Curve {28} = 36;
Transfinite Curve {29} = 37;

Line Loop (9) = {-30,-31,-32,-33};
Line Loop (10) = {-34,-35,-36,-37};
Line Loop (11) = {-38,-39,-40,-41};
Line Loop (12) = {-42,-43,-44,-45};
Line Loop (13) = {-10, -16, 37, -26, 32};
Line Loop (14) = {-15, -23, 22, -1, 41, -27, 36};
Line Loop (15) = {-2, -14, 45, -28, 40};
Line Loop (16) = {-20, 21, -24, 25, 33, -29, 44};

Plane Surface (9) = {9};
Plane Surface (10) = {10};
Plane Surface (11) = {11};
Plane Surface (12) = {12};
Plane Surface (13) = {13};
Plane Surface (14) = {14};
Plane Surface (15) = {15};
Plane Surface (16) = {16};

Transfinite Surface {9} = {16, 20, 27, 8};
Transfinite Surface {10} = {17, 21, 22, 12};
Transfinite Surface {11} = {19, 23, 24, 1};
Transfinite Surface {12} = {18, 25, 26, 11};
Transfinite Surface {13} = {21, 20, 12, 8};
Transfinite Surface {14} = {22, 23, 12, 1};
Transfinite Surface {15} = {24, 25, 1, 11};
Transfinite Surface {16} = {27, 26, 11, 8};

Transfinite Surface {1} = {1,2,3,4};
Transfinite Surface {2} = {2,4,6,14};
Transfinite Surface {3} = {6,7,5,14};
Transfinite Surface {4} = {6,9,13,7};
Transfinite Surface {5} = {7,13,8,10};
Transfinite Surface {6} = {3,11,15,4};
Transfinite Surface {7} = {15,9,6,4};
Transfinite Surface {8} = {7,10,12,5};

Recombine Surface {9, 10, 11, 12, 13, 14, 15, 16};
Physical Surface ("M1") = {9, 10, 11, 12, 13, 14, 15, 16};

Physical Curve("Top") = {31,26,34};
Physical Curve("Bottom") = {28,42,39};
Physical Curve("Left") = {43,29,30};
Physical Curve("Right") = {35,27,38};
