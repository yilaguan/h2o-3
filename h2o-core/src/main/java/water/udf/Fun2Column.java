package water.udf;

import water.fvec.Vec;
import water.udf.fp.Function2;
import water.udf.fp.Functions;

/**
 * This column depends on two other columns
 */
public class Fun2Column<X, Y, Z> extends FunColumnBase<Z> {
  private final Function2<X, Y, Z> f;
  private final Column<X> xs;
  private final Column<Y> ys;

  @Override public int rowLayout() { return xs.rowLayout(); }

  /**
   * deserialization :(
   */
  public Fun2Column() {
    f = null; xs = null; ys = null;
  }
  
  public Fun2Column(Function2<X, Y, Z> f, Column<X> xs, Column<Y> ys) {
    super(xs);
    this.f = f;
    this.xs = xs;
    this.ys = ys;
    assert xs.isCompatibleWith(ys) : "Columns must be compatible: " + xs + ", " + ys;
  }
  
  @Override public Z get(long position) { 
    return isNA(position) ? null : f.apply(xs.apply(position), ys.apply(position)); 
  }

  @Override
  public TypedChunk<Z> chunkAt(int i) {
    return new FunChunk(xs.chunkAt(i), ys.chunkAt(i));
  }

  @Override public boolean isNA(long i) { return xs.isNA(i) || ys.isNA(i); }

  /**
   * Pretends to be a chunk of a column, for distributed calculations.
   * Has type, and is not materialized
   */
  public class FunChunk extends DependentChunk<Z> {
    private final TypedChunk<X> cx;
    private final TypedChunk<Y> cy;

    @Override public Vec vec() { return Fun2Column.this.vec(); }

    public FunChunk(TypedChunk<X> cx, TypedChunk<Y> cy) {
      super(cx);
      this.cx = cx;
      this.cy = cy;
    }

    @Override public boolean isNA(long i) { return cx.isNA(i) || cy.isNA(i); }

    @Override public Z get(long i) { return f.apply(cx.get(i), cy.get(i)); }
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o instanceof Fun2Column) {
      Fun2Column other = (Fun2Column) o;
      return Functions.equal(f, other.f) && xs.equals(other.xs);
    }
    return false;

  }

  @Override
  public int hashCode() {
    return 61 * xs.hashCode() + Functions.hashCode(f);
  }

  @Override public String toString() { return "Fun2Column(" + f.getClass().getSimpleName() + "," + xs + "," + ys + ")"; }
}
