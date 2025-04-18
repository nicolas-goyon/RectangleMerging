@startuml
package "ConsoleAppExample" {
  class ExampleVoxel {
  }
  class Program {
  }
  class ExampleMesh {
    + Vertices: IReadOnlyList<(float x, float y, float z)>
    + Triangles: IReadOnlyList<int>
  }
  class ExampleChunk {
    + GetVoxels() : IEnumerable<ExampleVoxel>
    + Set(uint x,  uint y,  uint z,  ExampleVoxel voxel) : void
    + AreDifferentAxis(Axis major,  Axis middle,  Axis minor) : bool
  }
}
package "VoxelMeshOptimizer" {
  package "VoxelMeshOptimizer.Core" {
    interface MeshOptimizer {
      + Optimize(Chunk<Voxel> chunk) : Mesh
    }
    interface Voxel {
      + ID: ushort
      + IsSolid: bool
    }
    enum VoxelFace {
      None
      Zpos
      Zneg
      Xneg
      Xpos
      Ypos
      Yneg
    }
    enum Axis {
      X
      Y
      Z
    }
    enum AxisOrder {
      Ascending
      Descending
    }
    class AxisExtensions {
      + «static» ToVoxelFace(Axis axis,  AxisOrder axisOrder) : VoxelFace
      + «static» GetDepthFromAxis(Axis axis,  AxisOrder axisOrder,  uint x,  uint y,  uint z,  Chunk<Voxel> chunk) : uint
    }
    interface Chunk {
      + XDepth: uint
      + YDepth: uint
      + ZDepth: uint
      + ForEachCoordinate(Axis major,  AxisOrder majorAsc,  Axis middle,  AxisOrder middleAsc,  Axis minor,  AxisOrder minorAsc,  Action<uint ,  uint ,  uint > action) : void
      + Get(uint x,  uint y,  uint z) : T
      + GetDepth(Axis axis) : uint
      + IsOutOfBound(uint x,  uint y,  uint z) : bool
      + AreDifferentAxis(Axis major, Axis middle, Axis minor) : bool
    }
    interface Mesh {
    }
    class VoxelVisibilityMap {
      + GetVisibleFaces(uint x,  uint y,  uint z) : VoxelFace
    }
    package "VoxelMeshOptimizer.Core.OcclusionAlgorithms" {
      class VoxelOcclusionOptimizer {
      }
      interface Occluder {
        + ComputeVisiblePlanes() : VisibleFaces
      }
      package "VoxelMeshOptimizer.Core.OcclusionAlgorithms.Common" {
        class VisibleFaces {
          + PlanesByAxis: Dictionary<(Axis, AxisOrder), List<VisiblePlane>>
        }
        class VisiblePlane {
          + MajorAxis: Axis
          + MajorAxisOrder: AxisOrder
          + MiddleAxis: Axis
          + MiddleAxisOrder: AxisOrder
          + MinorAxis: Axis
          + MinorAxisOrder: AxisOrder
          + SliceIndex: uint
          + IsPlaneEmpty: bool
          + Describe() : string
        }
      }
    }
    package "VoxelMeshOptimizer.Core.OptimizationAlgorithms" {
      package "VoxelMeshOptimizer.Core.OptimizationAlgorithms.DisjointSet" {
        class DisjointSet2DOptimizer {
          + Optimize() : void
        }
        class DisjointSetMeshOptimizer {
        }
      }
    }
  }
}

VoxelOcclusionOptimizer --|> Occluder
DisjointSetMeshOptimizer --|> MeshOptimizer
ExampleVoxel --|> Voxel
ExampleMesh --|> Mesh
ExampleChunk --|> Chunk
AxisExtensions ..> Axis
AxisExtensions ..> VoxelFace
Chunk ..> Axis
DisjointSetMeshOptimizer ..> Chunk
DisjointSetMeshOptimizer ..> Voxel
ExampleChunk ..> ExampleVoxel
MeshOptimizer ..> Chunk
MeshOptimizer ..> Mesh
MeshOptimizer ..> Voxel
Occluder ..> VisibleFaces
VisibleFaces ..> Axis
VisibleFaces ..> AxisOrder
VisibleFaces ..> VisiblePlane
VisiblePlane ..> Axis
VisiblePlane ..> AxisOrder
VoxelVisibilityMap ..> VoxelFace
@enduml