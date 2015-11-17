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
		"rect" : [ 84.0, 104.0, 900.0, 552.0 ],
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
					"fontface" : 0,
					"fontsize" : 12.0,
					"id" : "obj-17",
					"linecount" : 21,
					"maxclass" : "o.display",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 45.0, 269.0, 150.0, 306.0 ],
					"text" : "/engine : \"moan\",\n/samples : \"Va-ord_pont-G#6-mf-1c.aif\",\n/suffix : \"_viola_moan.wav\",\n/time : 0.875971,\n/pitch : [1., 0., 1., 1.36251, 211.456, 0.0149355, 1.60296, 543.192, -0.687412, 1., 121.323, -0.523238],\n/amp : [0., 0., 1., 1., 197.678, -0.454194, 0.783072, 275.627, 0.232336, 0., 402.667, -0.0859687]",
					"textcolor" : [ 1.0, 1.0, 1.0, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"maxclass" : "newobj",
					"numinlets" : 1,
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
						"rect" : [ 141.0, 347.0, 1265.0, 480.0 ],
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
									"id" : "obj-21",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 46.0, 149.0, 75.0, 22.0 ],
									"style" : "",
									"text" : "moan_voice"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-20",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 46.0, 113.0, 75.0, 22.0 ],
									"style" : "",
									"text" : "moan_voice"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-13",
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "FullPacket" ],
									"patching_rect" : [ 46.0, 31.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-12",
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 46.0, 305.0, 30.0, 30.0 ],
									"style" : ""
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-6",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 46.0, 77.0, 75.0, 22.0 ],
									"style" : "",
									"text" : "moan_voice"
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-6", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-13", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-21", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-20", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-12", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-21", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-20", 0 ],
									"disabled" : 0,
									"hidden" : 0,
									"source" : [ "obj-6", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 45.0, 234.0, 57.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"style" : "",
						"tags" : ""
					}
,
					"style" : "",
					"text" : "p moans"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 206.0, 30.0, 24.0, 24.0 ],
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
									"saved_bundle_data" : [ 35, 98, 117, 110, 100, 108, 101, 0, -39, -10, 41, -40, 55, -31, -77, 66, 0, 0, 4, -72, 47, 115, 99, 111, 114, 101, 0, 0, 44, 46, 46, 46, 0, 0, 0, 0, 0, 0, 1, -120, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 109, 111, 97, 110, 0, 0, 0, 0, 0, 0, 0, 44, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 86, 99, 45, 112, 111, 110, 116, 95, 111, 114, 100, 45, 68, 53, 45, 109, 102, 45, 49, 99, 46, 97, 105, 102, 0, 0, 0, 0, 0, 0, 0, 28, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 99, 101, 108, 108, 111, 95, 109, 111, 97, 110, 46, 119, 97, 118, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 63, -20, 19, 77, -25, 51, -40, -112, 0, 0, 0, 120, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 64, 15, -108, -22, 61, -127, -25, 47, 64, 119, 39, 72, 106, 109, -22, 50, -65, -52, 34, -14, 20, 116, 89, 26, 64, 12, 39, -33, -120, 45, -94, 23, 64, 105, 25, 12, -50, 89, 91, -11, 63, -67, 122, -24, 114, 56, 126, -20, 63, -16, 0, 0, 0, 0, 0, 0, 64, 115, 33, -27, 85, -10, -86, -51, -65, -46, -51, -86, -30, -104, 110, 121, 0, 0, 0, 120, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -29, -19, 97, -30, -109, -48, -125, 64, 108, -28, 47, -99, 39, -53, 47, -65, -72, -89, 49, -90, 6, 42, 8, 63, -16, 0, 0, 0, 0, 0, 0, 64, 112, -27, -56, -99, -109, 67, -105, -65, -55, 18, 48, 45, 44, -24, -98, 0, 0, 0, 0, 0, 0, 0, 0, 64, 119, 125, -45, -69, 106, 25, -53, 63, -69, 83, -41, 1, -26, -46, -44, 0, 0, 1, -116, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 109, 111, 97, 110, 0, 0, 0, 0, 0, 0, 0, 44, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 86, 110, 45, 97, 114, 116, 45, 104, 97, 114, 109, 45, 65, 54, 45, 109, 102, 45, 51, 99, 46, 97, 105, 102, 0, 0, 0, 0, 0, 0, 0, 32, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 118, 105, 111, 108, 105, 110, 95, 109, 111, 97, 110, 46, 119, 97, 118, 0, 0, 0, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 63, -23, -34, -124, 96, 16, 47, 54, 0, 0, 0, 120, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -16, 102, -104, 126, -87, -125, -3, 64, 102, 17, 3, -69, 108, 97, -32, -65, -27, -65, -16, 89, 51, 7, 24, 63, -18, 35, 90, -53, 52, 60, -17, 64, 127, -36, 107, -48, -101, -85, 90, -65, -56, -128, -37, 0, 5, -17, 48, 63, -16, 0, 0, 0, 0, 0, 0, 64, 94, -122, -77, 117, 54, -1, -76, -65, -64, 45, -5, -99, -49, 15, 122, 0, 0, 0, 120, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -29, 5, -123, 56, -75, 28, 2, 64, 119, 84, -14, -24, 87, -105, 75, 63, -52, -115, -71, -112, 107, 118, 96, 63, -16, 0, 0, 0, 0, 0, 0, 64, 119, -120, -71, -101, -105, 86, 123, 63, -40, 6, 76, 22, -15, 113, -126, 0, 0, 0, 0, 0, 0, 0, 0, 64, 77, 71, 112, 61, -123, 115, 120, -65, -45, -7, -19, 110, -88, -69, 113, 0, 0, 1, -120, 35, 98, 117, 110, 100, 108, 101, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 47, 101, 110, 103, 105, 110, 101, 0, 44, 115, 0, 0, 109, 111, 97, 110, 0, 0, 0, 0, 0, 0, 0, 44, 47, 115, 97, 109, 112, 108, 101, 115, 0, 0, 0, 0, 44, 115, 0, 0, 86, 97, 45, 111, 114, 100, 95, 112, 111, 110, 116, 45, 71, 35, 54, 45, 109, 102, 45, 49, 99, 46, 97, 105, 102, 0, 0, 0, 0, 0, 0, 28, 47, 115, 117, 102, 102, 105, 120, 0, 44, 115, 0, 0, 95, 118, 105, 111, 108, 97, 95, 109, 111, 97, 110, 46, 119, 97, 118, 0, 0, 0, 0, 20, 47, 116, 105, 109, 101, 0, 0, 0, 44, 100, 0, 0, 63, -20, 7, -13, -7, -114, 115, -62, 0, 0, 0, 120, 47, 112, 105, 116, 99, 104, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -11, -52, -40, -92, -58, -38, 59, 64, 106, 110, -102, -109, -63, -13, 81, 63, -114, -106, -126, -5, -63, 68, -64, 63, -7, -91, -74, 122, -56, 126, 111, 64, -128, -7, -120, 112, -84, -84, 31, -65, -27, -1, 71, 27, -110, 21, -100, 63, -16, 0, 0, 0, 0, 0, 0, 64, 94, 84, -87, 96, -65, -96, -66, -65, -32, -66, 92, -65, -49, 121, 118, 0, 0, 0, 120, 47, 97, 109, 112, 0, 0, 0, 0, 44, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 63, -16, 0, 0, 0, 0, 0, 0, 64, 104, -75, -82, -105, 106, -36, 99, -65, -35, 17, -126, -15, -126, -105, -72, 63, -23, 14, -19, 122, -97, 85, 71, 64, 113, 58, 7, 18, 14, -63, 116, 63, -51, -67, 44, -44, -116, -5, -104, 0, 0, 0, 0, 0, 0, 0, 0, 64, 121, 42, -86, 37, -90, 10, 113, -65, -74, 2, 11, 50, 66, 47, 96, 0, 0, 0, 28, 47, 112, 114, 101, 102, 105, 120, 0, 44, 115, 0, 0, 49, 49, 49, 55, 49, 52, 51, 52, 48, 46, 48, 51, 53, 52, 0, 0 ],
									"saved_bundle_length" : 1260,
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
					"patching_rect" : [ 60.0, 60.0, 165.0, 22.0 ],
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
					"numoutlets" : 4,
					"outlettype" : [ "FullPacket", "FullPacket", "FullPacket", "FullPacket" ],
					"patching_rect" : [ 45.0, 182.0, 330.0, 22.0 ],
					"style" : "",
					"text" : "o.cond /engine == moan\\, /engine == perc\\, /engine == reartic"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "FullPacket" ],
					"patching_rect" : [ 155.0, 120.0, 88.0, 22.0 ],
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
					"patching_rect" : [ 45.0, 150.0, 129.0, 22.0 ],
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
					"patching_rect" : [ 45.0, 120.0, 83.0, 22.0 ],
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
					"patching_rect" : [ 45.0, 90.0, 129.0, 22.0 ],
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
					"patching_rect" : [ 45.0, 30.0, 151.0, 22.0 ],
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
					"destination" : [ "obj-17", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-15", 0 ]
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
					"destination" : [ "obj-4", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
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
					"destination" : [ "obj-15", 0 ],
					"disabled" : 0,
					"hidden" : 0,
					"source" : [ "obj-6", 0 ]
				}

			}
 ],
		"dependency_cache" : [ 			{
				"name" : "moan_voice.maxpat",
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
				"name" : "o.print.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "o.display.mxo",
				"type" : "iLaX"
			}
 ],
		"embedsnapshot" : 0
	}

}
