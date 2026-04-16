package ecommerce;

import org.junit.platform.suite.api.IncludeTags;
import org.junit.platform.suite.api.SelectPackages;
import org.junit.platform.suite.api.Suite;

@Suite
@SelectPackages("ecommerce")
@IncludeTags("fast")
public class FastTestSuite {
    // This class remains empty. It acts as a configuration holder to run only "fast" tests.
}