def intersection_calculation(start, point):
    vector = ((start[0] - point[0]), (start[1] - point[1]))
    line = [point, vector]

    atol_temp= 10**-11
    rtol_temp= 10**-11

    atol_temp_point= 10**-11
    rtol_temp_point= 10**-11
    
    x_direction = vector[0]/vector[0]
    y_direction = vector[1]/vector[1]

     l = LineString([(start[0], start[1]),(point[0],point[1])])

    i = self.circle.intersection(l)
    l2 = None
    start_count = 0
    #print( f'Line:{l} intersection:{i}')
    if str(type(i)) == "<class 'shapely.geometry.multipoint.MultiPoint'>":
        # Are there an even number of intersections? save the line to test for later
        intersections = len(list(i))
        list_of_points = list(i)
        for intsec_p in range(0, len(list_of_points)):
                # Does the point already exist on the circle? Return True 
                if (np.isclose(list_of_points[intsec_p].coords[0][0], start[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(list_of_points[intsec_p].coords[0][1], start[1], rtol=rtol_temp, atol=atol_temp)):
                    if start_count > 0:
                        intersections -= 2
                    start_count += 1
                elif np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(list_of_points[intsec_p].coords[0][1], point[1], rtol=rtol_temp, atol=atol_temp):
                    self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} point is not apart of the circle.')
                    return True
                elif (intsec_p < len(list_of_points)-1 
                and np.isclose(abs(list_of_points[intsec_p].coords[0][0]-list_of_points[intsec_p+1].coords[0][0]), 0,rtol=rtol_temp_point, atol=atol_temp_point) 
                and np.isclose(abs(list_of_points[intsec_p].coords[0][1]-list_of_points[intsec_p+1].coords[0][1]), 0, rtol=rtol_temp_point, atol=atol_temp_point)):
                    intersections -= 1

        if start_count > 1 and len(list_of_points) == 2 and intersections == 0:
            self.debug_point(point,True, f' Intersection:{i} number of intersections:{intersections} Point:{point} multiple intersections with start but in domain.')
            return False
        elif (point[1] > start[1] and 
        not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
        and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
        and intersections%2 == 0
        and intersections != 0):
            self.debug_point(point,True, f' Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections above line')
            return False
        elif (point[1] < start[1] and 
        not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
        and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
        and intersections%2 == 0):
            self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections below line')
            return True
        elif (point[1] > start[1] and 
        not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
        and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
        and intersections%2 == 1):
            self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections above line but in domain.')
            return True
        elif (point[1] < start[1] and 
        not np.isclose(list_of_points[intsec_p].coords[0][0], point[0],rtol=rtol_temp_point, atol=atol_temp_point)
        and not np.isclose(list_of_points[intsec_p].coords[0][1], point[1],rtol=rtol_temp_point, atol=atol_temp_point)  
        and intersections%2 == 1):
            self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections below line')
            return False
        else:
            return None

    elif str(type(i)) == "<class 'shapely.geometry.linestring.LineString'>":
        self.debug_point(point,True, f'False. Intersection:{i} Point:{point} Line is wrong')
        return False
    elif str(type(i)) == "<class 'shapely.geometry.point.Point'>":
        intersections = 1

        if np.isclose(i.coords[0][0], start[0],rtol=rtol_temp, atol=atol_temp) and np.isclose(i.coords[0][1], start[1], rtol=rtol_temp, atol=atol_temp):
            intersections -= 1
            return None

        if point[1] > start[1] and intersections%2 == 0:
            self.debug_point(point,False, f' Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections above line')
            return True
        elif point[1] < start[1] and intersections%2 == 0:
            self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Even intersections below line')
            return False
        elif point[1] > start[1] and intersections%2 == 1:
            self.debug_point(point,True, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections above line')
            return False
        elif point[1] <  start[1] and intersections%2 == 1:
            self.debug_point(point,False, f'Intersection:{i} number of intersections:{intersections} Point:{point} Odd intersections below line')
            return True

    elif str(type(i)) == "<class 'shapely.geometry.collection.GeometryCollection'>":
        #self.debug_point(point,True, f'False. Intersection:{i} Point:{point} point missed by shapelys intersections.')
        if point[1] > start[1]:
            return True
        elif point[1] <= start[1]:
            return False
    else:
        self.debug_point(point,True, f'False. Intersection:{i} Point:{point} type:{str(type(i))} Geometry object not accounted for')
        return None