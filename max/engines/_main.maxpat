{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 7,
			"minor" : 0,
			"revision" : 6,
			"architecture" : "x86",
			"modernui" : 1
		}
,
		"rect" : [ 82.0, 104.0, 1058.0, 671.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-17",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 517.0, 222.0, 24.0, 24.0 ],
					"presentation_rect" : [ 520.0, 224.0, 0.0, 0.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-16",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "FullPacket" ],
					"patching_rect" : [ 426.75, 198.0, 109.0, 22.0 ],
					"style" : "",
					"text" : "engine_inst reartic"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 388.0, 222.0, 24.0, 24.0 ],
					"presentation_rect" : [ 330.5, 241.0, 0.0, 0.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-11",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "FullPacket" ],
					"patching_rect" : [ 299.5, 198.0, 108.0, 22.0 ],
					"style" : "",
					"text" : "engine_inst rapids"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-37",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 226.25, 222.0, 24.0, 24.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-36",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 106.0, 222.0, 24.0, 24.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-32",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 696.0, 318.0, 24.0, 22.0 ],
					"style" : "",
					"text" : "t 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-31",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "bang", "float" ],
					"patching_rect" : [ 696.0, 270.0, 51.0, 22.0 ],
					"style" : "",
					"text" : "t bang f"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 696.0, 294.0, 51.0, 22.0 ],
					"style" : "",
					"text" : "delay"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-29",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "int", "" ],
					"patching_rect" : [ 596.0, 318.0, 30.0, 22.0 ],
					"style" : "",
					"text" : "t 1 l"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-28",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 596.0, 294.0, 82.0, 22.0 ],
					"style" : "",
					"text" : "append wave"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-27",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 596.0, 270.0, 85.0, 22.0 ],
					"style" : "",
					"text" : "prepend open"
				}

			}
, 			{
				"box" : 				{
					"fontface" : 0,
					"fontsize" : 12.0,
					"id" : "obj-26",
					"linecount" : 2,
					"maxclass" : "o.expr.codebox",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "FullPacket", "FullPacket" ],
					"patching_rect" : [ 596.0, 198.0, 279.0, 46.0 ],
					"text" : "/filename = /prefix + \"_global.wav\",\n/maxtime = /time * 1000. + 20.",
					"textcolor" : [ 0.0, 0.0, 0.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "FullPacket" ],
					"patching_rect" : [ 596.0, 246.0, 219.0, 22.0 ],
					"style" : "",
					"text" : "o.route /filename /maxtime"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 596.0, 378.0, 61.0, 22.0 ],
					"style" : "",
					"text" : "sfrecord~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-22",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "FullPacket", "FullPacket" ],
					"patching_rect" : [ 45.0, 150.0, 111.0, 22.0 ],
					"style" : "",
					"text" : "o.if bound(/engine)"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 132.666672, 289.0, 89.0, 22.0 ],
					"style" : "",
					"text" : "loadmess 127."
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "gain~",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 45.0, 313.0, 176.666672, 25.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "ezdac~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 45.0, 378.0, 45.0, 45.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "" ],
					"patching_rect" : [ 172.25, 198.0, 73.0, 22.0 ],
					"style" : "",
					"text" : "engine perc"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "" ],
					"patching_rect" : [ 45.0, 198.0, 80.0, 22.0 ],
					"style" : "",
					"text" : "engine moan"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 206.0, 28.0, 24.0, 24.0 ],
					"style" : ""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 7,
							"minor" : 0,
							"revision" : 6,
							"architecture" : "x86",
							"modernui" : 1
						}
,
						"rect" : [ 109.0, 129.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-5",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 67.0, 82.0, 91.0, 22.0 ],
									"style" : "",
									"text" : "loadmess clear"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-4",
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 67.0, 417.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-3",
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 575.0, 33.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-2",
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 67.0, 33.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"fontface" : 0,
									"fontsize" : 12.0,
									"id" : "obj-1",
									"maxclass" : "o.compose",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 67.0, 120.0, 538.0, 24.0 ],
									"saved_bundle_data" : [ 35, 98, 117, 110, 100, 108, 101, 0, -39, -2, 17, -6, -110, -23, -96, -105, 0, 0, 5, 108, 47, 115, 99, 111, 114, 101, 0, 0, 44, 46, 46, 46, 46, 0, 0, 0, 0, 0, 0, -16, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 112, 101, 114, 99, 0, 0, 0, 0, 0, 0, 0, 36, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 79, 98, 45, 115, 102, 122, 45, 71, 35, 52, 45, 102, 112, 46, 97, 105, 102, 0, 0, 0, 0, 0, 0, 28, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 111, 98, 111, 101, 95, 112, 101, 114, 99, 46, 119, 97, 118, 0, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 64, 15, 98, -108, -63, -8, -6, 18, 0, 0, 0, 20, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 0, 0, 63, -16, 79, 65, -10, -17, 120, 59, 0, 0, 0, 76, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 105, 100, 100, 100, 105, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -29, 79, -59, 33, -34, 113, 22, 0, 0, 0, 20, 63, -29, 79, -59, 33, -34, 113, 22, 64, -51, -5, 126, -54, 48, 4, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 1, 72, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 109, 111, 97, 110, 0, 0, 0, 0, 0, 0, 0, 40, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 86, 97, 45, 110, 111, 110, 118, 105, 98, 45, 67, 55, 45, 102, 102, 45, 49, 99, 46, 97, 105, 102, 0, 0, 0, 0, 0, 28, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 118, 105, 111, 108, 97, 95, 109, 111, 97, 110, 46, 119, 97, 118, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 64, 9, -48, 21, 49, 59, -38, -111, 0, 0, 0, 60, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 100, 105, 100, 100, 100, 0, 63, -8, -108, -39, 13, 20, -1, -120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 63, -11, 91, -127, 8, -16, -20, 94, 64, -87, 53, 52, -78, 20, 115, 114, 63, -57, -31, -79, -99, 110, 122, -110, 0, 0, 0, 120, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -24, -105, 110, 23, 99, 11, 84, 64, -103, 86, -14, -67, 113, 122, 22, 63, -71, -16, -107, -110, -62, 29, 48, 63, -16, 0, 0, 0, 0, 0, 0, 64, -111, 101, 10, -33, 10, -64, -75, -65, -51, -4, 13, -89, 28, -40, 42, 0, 0, 0, 0, 0, 0, 0, 0, 64, 126, -71, -81, 30, -78, -80, 98, -65, -63, -28, -49, 40, -52, 26, 4, 0, 0, 1, -120, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 109, 111, 97, 110, 0, 0, 0, 0, 0, 0, 0, 44, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 86, 99, 45, 116, 114, 101, 109, 95, 111, 114, 100, 45, 65, 51, 45, 109, 102, 45, 50, 99, 46, 97, 105, 102, 0, 0, 0, 0, 0, 0, 0, 28, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 99, 101, 108, 108, 111, 95, 109, 111, 97, 110, 46, 119, 97, 118, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 64, 9, 34, 6, -36, 46, -74, 10, 0, 0, 0, 120, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 63, -18, 52, 55, -25, 16, 19, 67, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -17, 34, -21, -86, -18, -100, 116, 64, -110, 2, 33, -76, -127, 64, -44, -65, -47, -92, -8, 33, -85, -33, 56, 63, -21, -89, -81, 104, 36, 1, -80, 64, -107, 24, 122, -81, 54, 27, -66, 63, -31, 64, -91, -31, -37, 87, 68, 63, -18, 52, 55, -25, 16, 19, 67, 64, -125, -9, -78, 4, -89, -67, -13, -65, -49, 24, -119, 30, 34, 114, 92, 0, 0, 0, 120, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -30, -116, -92, 16, -13, -81, 104, 64, -104, -8, 104, -51, 24, 53, -7, 63, -30, -69, 55, -126, -69, -24, 37, 63, -16, 0, 0, 0, 0, 0, 0, 64, -108, 53, 25, 60, -127, -118, 82, -65, -25, -90, 115, 103, -73, 3, 74, 0, 0, 0, 0, 0, 0, 0, 0, 64, 111, 71, -102, -29, -117, -38, 13, -65, -28, 111, 109, 87, 8, 14, 28, 0, 0, 1, -116, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 109, 111, 97, 110, 0, 0, 0, 0, 0, 0, 0, 44, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 86, 110, 45, 97, 114, 116, 45, 104, 97, 114, 109, 45, 71, 35, 55, 45, 109, 102, 45, 49, 99, 46, 97, 105, 102, 0, 0, 0, 0, 0, 0, 32, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 118, 105, 111, 108, 105, 110, 95, 109, 111, 97, 110, 46, 119, 97, 118, 0, 0, 0, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 64, 10, -109, -19, 11, -13, -37, -3, 0, 0, 0, 120, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 63, -17, -2, 77, 56, -23, 81, 71, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -15, -19, 114, -49, -62, -60, -13, 64, -115, -124, -66, -117, 100, -41, 97, 63, -37, -36, 28, 55, -109, -109, -88, 63, -17, -85, -50, -83, -13, 21, -94, 64, -97, 68, -10, -81, -52, 86, -84, 63, -44, -72, 101, -29, -121, 39, -116, 63, -17, -2, 77, 56, -23, 81, 71, 64, 119, -122, 84, 23, 102, 29, 56, 63, -81, -58, -94, 19, 87, 32, -32, 0, 0, 0, 120, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -27, 39, -13, 1, 82, -4, 124, 64, -110, 22, 47, 83, 13, -83, 72, -65, -31, 61, -78, 21, 93, -93, -66, 63, -16, 0, 0, 0, 0, 0, 0, 64, -103, 86, 43, -39, -89, 86, 74, 63, -25, 14, 89, -38, -30, 34, 92, 0, 0, 0, 0, 0, 0, 0, 0, 64, -128, -7, 31, -99, 70, -116, 50, 63, -33, -91, 39, 33, 80, 101, 91, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 64, 19, -79, 74, 96, -4, 125, 9, 0, 0, 0, 28, 47, 112, 114, 101, 102, 105, 120, 0, 44, 115, 0, 0, 49, 49, 50, 51, 49, 52, 51, 48, 49, 56, 46, 48, 57, 54, 52, 0 ],
									"saved_bundle_length" : 1464,
									"textcolor" : [ 0.188, 0.188, 0.188, 1.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-4", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-1", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-1", 1 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-2", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-1", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-3", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-1", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-5", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 60.0, 54.0, 165.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"style" : "",
						"tags" : ""
					}
,
					"style" : "",
					"text" : "p last_score"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 5,
					"outlettype" : [ "FullPacket", "FullPacket", "FullPacket", "FullPacket", "FullPacket" ],
					"patching_rect" : [ 45.0, 174.0, 528.0, 22.0 ],
					"style" : "",
					"text" : "o.cond /engine == moan\\, /engine == perc\\, /engine == rapids\\, /engine == reartic"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "FullPacket" ],
					"patching_rect" : [ 155.0, 102.0, 88.0, 22.0 ],
					"style" : "",
					"text" : "o.select /prefix"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "FullPacket" ],
					"patching_rect" : [ 45.0, 126.0, 129.0, 22.0 ],
					"style" : "",
					"text" : "o.union"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-3",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "FullPacket" ],
					"patching_rect" : [ 45.0, 102.0, 83.0, 22.0 ],
					"style" : "",
					"text" : "o.route /value"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 45.0, 78.0, 129.0, 22.0 ],
					"style" : "",
					"text" : "o.listenumerate /score"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 45.0, 30.0, 159.0, 22.0 ],
					"style" : "",
					"text" : "udpreceive 56765 CNMAT"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 54.5, 364.0, 605.5, 364.0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 54.5, 364.0, 80.5, 364.0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 54.5, 340.0, 54.5, 340.0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-11", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-11", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 142.166672, 311.0, 54.5, 311.0 ],
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-17", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-16", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 164.5, 102.0, 174.0, 102.0, 174.0, 87.0, 605.5, 87.0 ],
					"source" : [ "obj-2", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-3", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-2", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-2", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-22", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-27", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-24", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-31", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-24", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-26", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-28", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-27", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-29", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-28", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 616.5, 364.0, 605.5, 364.0 ],
					"source" : [ "obj-29", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-29", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-32", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-31", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-31", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"midpoints" : [ 705.5, 364.0, 605.5, 364.0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-22", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 1 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-11", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-16", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 3 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-36", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-7", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-10", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-8", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-8", 1 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "engine.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "_voice.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "moan.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "perc.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "engine_inst.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "_voice_inst.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "rapids.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "reartic.maxpat",
				"bootpath" : "~/Documents/music/THIRST/max/engines",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "o.listenumerate.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.route.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.union.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.select.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.cond.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.compose.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.pack.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.expr.codebox.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.if.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.timetag.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.schedule.mxo",
				"type" : "iLaX"
			}
 ],
		"embedsnapshot" : 0
	}

}
