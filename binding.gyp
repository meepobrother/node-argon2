{
  "targets": [{
    "target_name": "argon2",
    "sources": ["src/argon2_node.cpp"],
    "cflags+": ["-Wno-cast-function-type"],
    "include_dirs+": ["<!(node -e \"require('nan')\")"],
    "link_settings": {
      "libraries": ["-largon2"],
    },
    "conditions": [
      ["OS == 'mac'", {
        "xcode_settings": {
          "MACOSX_DEPLOYMENT_TARGET": "10.9",
        }
      }]
    ],
    "configurations": {
      "Debug": {
        "conditions": [
          ["OS == 'linux'", {
            "cflags": ["--coverage"],
            "ldflags": ["-fprofile-arcs", "-ftest-coverage"],
          }]
        ]
      },
      "Release": {
        "target_conditions": [
          ["OS != 'win'", {
            "cflags+": ["-fdata-sections", "-ffunction-sections", "-fvisibility=hidden"],
            "ldflags+": ["-Wl,--gc-sections"]
          }]
        ],
        "defines+": ["_FORTIFY_SOURCE=2", "NDEBUG"]
      },
    },
  }]
}
