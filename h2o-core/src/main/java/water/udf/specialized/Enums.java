package water.udf.specialized;

import com.google.common.collect.Sets;
import water.fvec.Chunk;
import water.fvec.Frame;
import water.fvec.Vec;
import water.udf.*;
import water.udf.fp.Function;
import water.udf.fp.Functions;

import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.Set;

import static water.udf.specialized.Integers.*;

/**
 * Specialized factory for enums (aka Cats)
 */
public class Enums extends DataColumns.BaseFactory<Integer, EnumColumn> {
  final String[] domain;
  
  /**
   * deserialization :(
   */
  public Enums() {
    super(Vec.T_CAT, "Cats");
    domain = null;
  }

  public Enums(String[] domain) {
    super(Vec.T_CAT, "Cats");
    this.domain = domain;
  }

  public static Enums enums(String[] domain) {
    return new Enums(domain);
  }

  public static ColumnFactory<Integer, EnumColumn> enumsAlt(String[] domain) {
    return enums(domain);
  }

  @Override
  public DataChunk<Integer> apply(final Chunk c) {
    return new IntegerChunk(c);
  }

  public EnumColumn newColumn(long length, final Function<Long, Integer> f) throws IOException {
    return new SingleColumnFrame.EnumFrame(length, f, domain).newColumn();
  }

  public EnumColumn newColumn(List<Integer> source) throws IOException {
    return new SingleColumnFrame.EnumFrame(source.size(), Functions.onList(source), domain).newColumn();
  }
  
  @Override
  public EnumColumn newColumn(final Vec vec) {
    if (vec.get_type() != Vec.T_CAT)
      throw new IllegalArgumentException("Expected type T_CAT, got " + vec.get_type_str());
    vec.setDomain(domain);
    return new EnumColumn(vec);
  }

  static Frame oneHotEncoding(String name, Vec vec) throws IOException {
    EnumColumn enumColumn = new EnumColumn(vec);
    UnfoldingFrame<Integer, DataColumn<Integer>> plain = enumColumn.oneHotEncodedFrame(name);
    return plain.materialize();
  }
  
  public static Frame oneHotEncoding(Frame dataset, String[] skipCols) throws IOException {
    Set<String> skipit = (skipCols == null) ? Collections.EMPTY_SET : Sets.newHashSet(skipCols);
    Frame output = new Frame();
    
    for(String colName : dataset.names()) {
      final Vec vec = dataset.vec(colName);
      if (skipit.contains(colName)) {
        output.add(colName, vec);
      } else {
        output.add(oneHotEncoding(colName, vec));
      }
    }
    return output;
  }

}
