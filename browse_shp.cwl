cwlVersion: v1.2
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: eforoutan/browse_shp:latest
  NetworkAccess:
    networkAccess: true

inputs:
  input_shapefile:
    type: Directory
    inputBinding:
      position: 1

outputs:
  FiedType:
    type: File  
    outputBinding:
      glob: "fields_and_types.csv"