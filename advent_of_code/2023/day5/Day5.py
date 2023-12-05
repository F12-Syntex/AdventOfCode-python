import os

class Day4:
    def __init__(self):
        self.input_content = None

    def solve_part1(self):
        
        seeds = self.parseContent()[0]
            
        minLocation = float("inf")
                                        
        for seed in seeds:
            minLocation = min(minLocation, self.computeSeed(seed))

        return minLocation
    
    def computeSeed(self, seed):
        _, seedsToSoil, soilToFertiliser, fertilizerToWater, waterToLight, lightToTempreture, temperatureToHumidity, humidityToLocation = self.parseContent()
        
        soilNumber = self.mapSeedToComponent(seed, seedsToSoil)
        fertilizerNumber = self.mapSeedToComponent(soilNumber, soilToFertiliser)  
        waterNumber = self.mapSeedToComponent(fertilizerNumber, fertilizerToWater)
        lightNumber = self.mapSeedToComponent(waterNumber, waterToLight)
        temperatureNumber = self.mapSeedToComponent(lightNumber, lightToTempreture)
        humidityNumber = self.mapSeedToComponent(temperatureNumber, temperatureToHumidity)
        locationNumber = self.mapSeedToComponent(humidityNumber, humidityToLocation)
        
        return locationNumber
    
    def solve_part2(self):
        seeds, seedsToSoil, soilToFertiliser, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation = self.parseContent()
        
        initialRanges = [(start, start + end) for start, end in zip(seeds[::2], seeds[1::2])]

        for mappings in [seedsToSoil, soilToFertiliser, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation]:
            newRanges = []
            
            for start, end in initialRanges:
                currentRange = [(start, end)]
                for dest, src, length in mappings:
                    srcEnd = src + length
                    nextRange = []
                    while currentRange:
                        currentRangeStart, currentRangeEnd = currentRange.pop(0)
                        left = (currentRangeStart, min(currentRangeEnd, src))
                        intersection = (max(currentRangeStart, src), min(srcEnd, currentRangeEnd))
                        right = (max(srcEnd, currentRangeStart), currentRangeEnd)
                        
                        #these ranges don't intersect, so process them for a different mapping
                        if left[1] > left[0]:
                            nextRange.append(left)
                        if right[1] > right[0]:
                            nextRange.append(right)
                            
                        #this stuff intersects with the current mapping, so just add the low and high bounds to our range
                        if intersection[1] > intersection[0]:
                            newRanges.append((intersection[0] - src + dest, intersection[1] - src + dest))
                            
                    currentRange = nextRange
                newRanges += currentRange
            
            initialRanges = newRanges
        
        #we don't use r[1] because that's going to be the upper bonud for that range, which is going to be more than r[0] anyway
        minLocation = min(r[0] for r in initialRanges)
        return minLocation


    
    
    def mapSeedToComponent(self, seedNumber, mappings):
        res = seedNumber
        for mapping in mappings:
            seed = self.mapComponent(seedNumber, mapping)
            res = seed if seed != seedNumber else res
        return res
    
    def mapComponent(self, sourceNumber, mappings):
        destStart = mappings[0]
        sourceStart = mappings[1]
        length = mappings[2]
        
        startRange = sourceStart
        endRange = sourceStart + length - 1
        
        if sourceNumber < startRange or sourceNumber > endRange:
            return sourceNumber
        
        offset = sourceNumber - startRange
        mapped = destStart + offset
                    
        return mapped
    
        
    
    def parseContent(self):
        
        seeds = self.toIntArr(self.input_content.split("seeds:")[1].split("\n")[0].split())
        
        seedsToSoil = self.input_content.split("seed-to-soil map:")[1].split("soil-to-fertilizer map:")[0].split("\n")
        seedsToSoil = [self.toIntArr(item.split(" ")) for item in seedsToSoil if item]
        
        seedsToFertilizer = self.input_content.split("soil-to-fertilizer map:")[1].split("fertilizer-to-water map:")[0].split("\n")
        seedsToFertilizer = [self.toIntArr(item.split(" ")) for item in seedsToFertilizer if item]
        
        fertilizerToWater = self.input_content.split("fertilizer-to-water map:")[1].split("water-to-light map:")[0].split("\n")
        fertilizerToWater = [self.toIntArr(item.split(" ")) for item in fertilizerToWater if item]
        
        waterToLight = self.input_content.split("water-to-light map:")[1].split("light-to-temperature map:")[0].split("\n")
        waterToLight = [self.toIntArr(item.split(" ")) for item in waterToLight if item]
        
        lightToTempreture = self.input_content.split("light-to-temperature map:")[1].split("temperature-to-humidity map:")[0].split("\n")
        lightToTempreture = [self.toIntArr(item.split(" ")) for item in lightToTempreture if item]
        
        temperatureToHumidity = self.input_content.split("temperature-to-humidity map:")[1].split("humidity-to-location map:")[0].split("\n")
        temperatureToHumidity = [self.toIntArr(item.split(" ")) for item in temperatureToHumidity if item] 
    
        humidityToLocation = self.input_content.split("humidity-to-location map:")[1].split("\n")
        humidityToLocation = [self.toIntArr(item.split(" ")) for item in humidityToLocation if item]      
        
        

        return seeds, seedsToSoil, seedsToFertilizer, fertilizerToWater, waterToLight, lightToTempreture, temperatureToHumidity, humidityToLocation
    
    def toIntArr(self, arr):
        return [int(char) for char in arr if str(char).isdigit()]


    def loadInputFiles(self):
        inputPath = os.path.join(os.getcwd(), "advent_of_code", "2023", "day5", "input.txt")
        with open(inputPath, "r") as f:
            self.input_content = f.read()

solver = Day4()
solver.loadInputFiles()
part1_result = solver.solve_part1()
part2_result = solver.solve_part2()

print("Solution to Part 1:", part1_result)
print("Solution to Part 2:", part2_result)
