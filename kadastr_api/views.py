from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json


def none_sum(*args):
    args = [a for a in args if not a is None]
    return sum(args) if args else 0


def kadastr_data(prefix):
    url = f"https://api.agro.uz/gis_bridge/readall?prefix={prefix}"
    response = requests.request("GET", url)
    return json.loads(response.text)


class KadastrAPIView(APIView):
    def get(self, request, prefix):
        api = kadastr_data(prefix)
        api.pop(-1)
        legal_area = 0
        total_farmland_areas = 0
        farmland_areas_with_water = 0
        total_arable_areas = 0
        arable_areas_with_water = 0
        arable_areas_without_wtr = 0
        total_pernnial_plant_ars = 0
        bad_land_area = 0
        hayfields_areas = 0
        pastures_areas = 0
        pastures_areas_with_water = 0
        backyard_lands_areas = 0
        reclamatn_preparatn_ars = 0
        total_forestry_areas = 0
        shrubbery_areas = 0
        unused_other_areas = 0
        gardens_areas = 0
        vineyards_areas = 0
        mulberry_trees_areas = 0
        othr_perenial_plants_ars = 0
        shelterbelts_areas = 0
        total_underwater_areas = 0
        roads_and_trails_areas = 0
        construction_land_area = 0
        al_lnd_nusd_agrcultr_ars = 0
        for i in api:
            legal_area = none_sum(legal_area, i.get('legal_area'))  # 8
            total_farmland_areas = none_sum(total_farmland_areas, i.get('total_farmland_areas'))  # 37
            farmland_areas_with_water = none_sum(farmland_areas_with_water, i.get('farmland_areas_with_water'))  # 18
            total_arable_areas = none_sum(total_arable_areas, i.get('total_arable_areas'))  # 34
            arable_areas_with_water = none_sum(arable_areas_with_water, i.get('arable_areas_with_water'))  # 13
            arable_areas_without_wtr = none_sum(arable_areas_without_wtr, i.get('arable_areas_without_wtr'))  # 14
            total_pernnial_plant_ars = none_sum(total_pernnial_plant_ars, i.get('total_pernnial_plant_ars'))  # 40
            bad_land_area = none_sum(bad_land_area, i.get('bad_land_area'))  # 48
            hayfields_areas = none_sum(hayfields_areas, i.get('hayfields_areas'))  # 21
            pastures_areas = none_sum(pastures_areas, i.get('pastures_areas'))  # 39
            pastures_areas_with_water = none_sum(pastures_areas_with_water, i.get('pastures_areas_with_water'))  # 26
            backyard_lands_areas = none_sum(backyard_lands_areas, i.get('backyard_lands_areas'))  # 47
            reclamatn_preparatn_ars = none_sum(reclamatn_preparatn_ars, i.get('reclamatn_preparatn_ars'))  # 28
            total_forestry_areas = none_sum(total_forestry_areas, i.get('total_forestry_areas'))  # 38
            shrubbery_areas = none_sum(shrubbery_areas, i.get('shrubbery_areas'))  # 32
            unused_other_areas = none_sum(unused_other_areas, i.get('unused_other_areas'))  # 42
            gardens_areas = none_sum(gardens_areas, i.get('gardens_areas'))  # 19
            vineyards_areas = none_sum(vineyards_areas, i.get('vineyards_areas'))  # 43
            mulberry_trees_areas = none_sum(mulberry_trees_areas, i.get('mulberry_trees_areas'))  # 24
            othr_perenial_plants_ars = none_sum(othr_perenial_plants_ars, i.get('othr_perenial_plants_ars'))  # 25
            shelterbelts_areas = none_sum(shelterbelts_areas, i.get('shelterbelts_areas'))  # 31
            total_underwater_areas = none_sum(total_underwater_areas, i.get('total_underwater_areas'))  # 41
            roads_and_trails_areas = none_sum(roads_and_trails_areas, i.get('roads_and_trails_areas'))  # 30
            construction_land_area = none_sum(construction_land_area, i.get('construction_land_area'))  # 50
            al_lnd_nusd_agrcultr_ars = none_sum(al_lnd_nusd_agrcultr_ars, i.get('al_lnd_nusd_agrcultr_ars'))  # 45

        if legal_area is None:
            legal_area = 0
        if total_farmland_areas is None:
            total_farmland_areas = 0
        if farmland_areas_with_water is None:
            farmland_areas_with_water = 0
        if total_arable_areas is None:
            total_arable_areas = 0
        if arable_areas_with_water is None:
            arable_areas_with_water = 0
        if arable_areas_without_wtr is None:
            arable_areas_without_wtr = 0
        if total_pernnial_plant_ars is None:
            total_pernnial_plant_ars = 0
        if bad_land_area is None:
            bad_land_area = 0
        if hayfields_areas is None:
            hayfields_areas = 0
        if pastures_areas is None:
            pastures_areas = 0
        if pastures_areas_with_water is None:
            pastures_areas_with_water = 0
        if backyard_lands_areas is None:
            backyard_lands_areas = 0
        if reclamatn_preparatn_ars is None:
            reclamatn_preparatn_ars = 0
        if total_forestry_areas is None:
            total_forestry_areas = 0
        if shrubbery_areas is None:
            shrubbery_areas = 0
        if unused_other_areas is None:
            unused_other_areas = 0
        if gardens_areas is None:
            gardens_areas = 0
        if vineyards_areas is None:
            vineyards_areas = 0
        if mulberry_trees_areas is None:
            mulberry_trees_areas = 0
        if othr_perenial_plants_ars is None:
            othr_perenial_plants_ars = 0
        data = {
            "total_land_area_full_total": round(legal_area, 2),  # 1
            "total_land_area_full_irrigated": '',  # 2
            "total_land_area_full_non_irrigated": '',  # 3
            "types_of_agricultural_land_total": round(total_farmland_areas, 2),  # 4
            "types_of_agricultural_land_irrigated": round(farmland_areas_with_water, 2),  # 5
            "types_of_agricultural_land_non_irrigated": round(total_farmland_areas - farmland_areas_with_water, 2),  # 6
            "cultivated_lands_total": round(total_arable_areas, 2),  # 7
            "cultivated_lands_irrigated": round(arable_areas_with_water, 2),  # 8
            "cultivated_lands_non_irrigated": round(arable_areas_without_wtr, 2),  # 9
            "perennial_trees_total": round(total_pernnial_plant_ars, 2),  # 10
            "gardens_areas": round(gardens_areas, 2),  # 10_onclick
            "vineyards_areas": round(vineyards_areas, 2),  # 10_onclick
            "mulberry_trees_areas": round(mulberry_trees_areas, 2),  # 10_onclick
            "othr_perenial_plants_ars": round(othr_perenial_plants_ars, 2),  # 10_onclick
            "perennial_trees_irrigated": '',  # 11
            "perennial_trees_non_irrigated": '',  # 12
            "gray_lands_total": round(bad_land_area, 2),  # 13
            "gray_lands_irrigated": '',  # 14
            "gray_lands_non_irrigated": '',  # 15
            "hayfield_pastures_total": round(hayfields_areas + pastures_areas, 2),  # 16
            "hayfield_pastures_irrigated": round(pastures_areas_with_water, 2),  # 17
            "hayfield_pastures_non_irrigated": round((hayfields_areas + pastures_areas) - pastures_areas_with_water, 2),
            # 18
            "lands_and_horticultural_associations_total": round(backyard_lands_areas, 2),  # 19
            "lands_and_horticultural_associations_full_irrigated": '',  # 20
            "lands_in_reclamation_condition": round(reclamatn_preparatn_ars, 2),  # 21
            "forests_total": round(total_forestry_areas, 2),  # 22
            "forests_irrigated": '',  # 23
            "shrubbery": round(shrubbery_areas, 2),  # 24
            "other_areas": round(shelterbelts_areas + total_underwater_areas + roads_and_trails_areas +
                                 construction_land_area + al_lnd_nusd_agrcultr_ars + unused_other_areas, 2),  # 25
            "shelterbelts_areas": round(shelterbelts_areas, 2),  # 25onclick
            "total_underwater_areas": round(total_underwater_areas, 2),  # 25onclick
            "roads_and_trails_areas": round(roads_and_trails_areas, 2),  # 25onclick
            "construction_land_area": round(construction_land_area, 2),  # 25onclick
            "al_lnd_nusd_agrcultr_ars": round(al_lnd_nusd_agrcultr_ars, 2),  # 25onclick
            "unused_other_areas": round(unused_other_areas, 2)  # 25onclick
        }
        return Response({
            'data': data
        })
