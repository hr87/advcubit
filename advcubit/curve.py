""" Module for curve operations and creation

This module contains functions to create special kind of curves
"""

import advcubit.system as _system
import advcubit.functions as _functions


def lastCurve():
    """ Obtaines the last created curve

    :return: last created curve
    """
    lastId = _system.cubitModule.get_last_id('curve')
    try:
        return _system.cubitModule.curve(lastId)
    except RuntimeError as e:
        _system.warning('Cannot retrieve last created surface!\n' + str(e))
        return None


def createArc(centerVertex, startVertex, endVertex):
    """ Creates an arc from 3 already created vertices

    :param centerVertex: Vertex at the center of the arc
    :param startVertex: Vertex at the start of the arc
    :param endVertex: Vertex at the end of the arc
    :return: None
    """
    _system.cubitCmd('Create Curve Arc Center Vertex {0} {1} {2}'.format(centerVertex.id(),
                                                                         startVertex.id(), endVertex.id()))
    return lastCurve()


def createCircle(radius, z=0.0):
    """ Creates a cirle in the xy plane

    :param radius: circle radius
    :param z: z offset
    :return: created curve
    """
    vertexCenter = _system.cubitModule.create_vertex(0, 0, z)
    vertexOuter = _system.cubitModule.create_vertex(radius, 0, z)
    return createArc(vertexCenter, vertexOuter, vertexOuter)


def createLine(point1, point2):
    """ Creates a straight curve between two points

    :param point1: start point in list/tuple form
    :param point2: end point in list/tuple form
    :return: created curve
    """
    point1 = _system.cubitModule.create_vertex(point1[0], point1[1], point1[2])
    point2 = _system.cubitModule.create_vertex(point2[0], point2[1], point2[2])

    return _system.cubitModule.create_curve(point1, point2)


def tangentCurve(baseCurves, tangent, point=(0.0, 0.0, 0.0), prec=2):
    """

    :param baseCurves: list of Curves
    :param tangent: tangent to compare against
    :param point: point for tangent
    :param prec: number of digits to compare
    :return: list of curves
    """
    curves = []
    for curve in baseCurves:
        surfaceTangent = curve.tangent(point)
        if _functions.roundTuple(surfaceTangent, prec) == _functions.roundTuple(tangent, prec):
            curves.append(curve)
    return curves


def sortCurves(curves):
    """ Sorts a list of curves by length

    :param curves: list of curves
    :return: new list of sorted curves
    """
    sortedCurves = sorted(curves, cmp=lambda x, y: cmp(x.lenght(), y.length()))
    return sortedCurves
