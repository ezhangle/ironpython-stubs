# encoding: utf-8
# module System.Windows.Shapes calls itself Shapes
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Shape(FrameworkElement, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """ Provides a base class for shape elements, such as System.Windows.Shapes.Ellipse, System.Windows.Shapes.Polygon, and System.Windows.Shapes.Rectangle. """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Shape, finalSize: Size) -> Size
        
            Arranges a System.Windows.Shapes.Shape by evaluating its 
             System.Windows.Shapes.Shape.RenderedGeometry and 
             System.Windows.Shapes.Shape.Stretch properties.
        
        
            finalSize: The final evaluated size of the System.Windows.Shapes.Shape.
            Returns: The final size of the arranged System.Windows.Shapes.Shape element.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Shape, constraint: Size) -> Size
        
            Measures a System.Windows.Shapes.Shape during the first layout pass prior to 
             arranging it.
        
        
            constraint: A maximum System.Windows.Size to not exceed.
            Returns: The maximum System.Windows.Size for the System.Windows.Shapes.Shape.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: Shape, drawingContext: DrawingContext)
            Provides a means to change the default appearance of a 
             System.Windows.Shapes.Shape element.
        
        
            drawingContext: A System.Windows.Media.DrawingContext object that is drawn during the rendering 
             pass of this System.Windows.Shapes.Shape.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the System.Windows.Media.Geometry of the System.Windows.Shapes.Shape.

"""

    Fill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush that specifies how the shape's interior is painted.

Get: Fill(self: Shape) -> Brush

Set: Fill(self: Shape) = value
"""

    GeometryTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents a System.Windows.Media.Transform that is applied to the geometry of a System.Windows.Shapes.Shape prior to when it is drawn.

Get: GeometryTransform(self: Shape) -> Transform

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    RenderedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that represents the final rendered System.Windows.Media.Geometry of a System.Windows.Shapes.Shape.

Get: RenderedGeometry(self: Shape) -> Geometry

"""

    Stretch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.Stretch enumeration value that describes how the shape fills its allocated space.

Get: Stretch(self: Shape) -> Stretch

Set: Stretch(self: Shape) = value
"""

    Stroke = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush that specifies how the System.Windows.Shapes.Shape outline is painted.

Get: Stroke(self: Shape) -> Brush

Set: Stroke(self: Shape) = value
"""

    StrokeDashArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a collection of System.Double values that indicate the pattern of dashes and gaps that is used to outline shapes.

Get: StrokeDashArray(self: Shape) -> DoubleCollection

Set: StrokeDashArray(self: Shape) = value
"""

    StrokeDashCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.PenLineCap enumeration value that specifies how the ends of a dash are drawn.

Get: StrokeDashCap(self: Shape) -> PenLineCap

Set: StrokeDashCap(self: Shape) = value
"""

    StrokeDashOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Double that specifies the distance within the dash pattern where a dash begins.

Get: StrokeDashOffset(self: Shape) -> float

Set: StrokeDashOffset(self: Shape) = value
"""

    StrokeEndLineCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.PenLineCap enumeration value that describes the System.Windows.Shapes.Shape at the end of a line.

Get: StrokeEndLineCap(self: Shape) -> PenLineCap

Set: StrokeEndLineCap(self: Shape) = value
"""

    StrokeLineJoin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.PenLineJoin enumeration value that specifies the type of join that is used at the vertices of a System.Windows.Shapes.Shape.

Get: StrokeLineJoin(self: Shape) -> PenLineJoin

Set: StrokeLineJoin(self: Shape) = value
"""

    StrokeMiterLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a limit on the ratio of the miter length to half the System.Windows.Shapes.Shape.StrokeThickness of a System.Windows.Shapes.Shape element.

Get: StrokeMiterLimit(self: Shape) -> float

Set: StrokeMiterLimit(self: Shape) = value
"""

    StrokeStartLineCap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.PenLineCap enumeration value that describes the System.Windows.Shapes.Shape at the start of a System.Windows.Shapes.Shape.Stroke.

Get: StrokeStartLineCap(self: Shape) -> PenLineCap

Set: StrokeStartLineCap(self: Shape) = value
"""

    StrokeThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width of the System.Windows.Shapes.Shape outline.

Get: StrokeThickness(self: Shape) -> float

Set: StrokeThickness(self: Shape) = value
"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


    FillProperty = None
    StretchProperty = None
    StrokeDashArrayProperty = None
    StrokeDashCapProperty = None
    StrokeDashOffsetProperty = None
    StrokeEndLineCapProperty = None
    StrokeLineJoinProperty = None
    StrokeMiterLimitProperty = None
    StrokeProperty = None
    StrokeStartLineCapProperty = None
    StrokeThicknessProperty = None


class Ellipse(Shape, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Draws an ellipse.
    
    Ellipse()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """ ArrangeOverride(self: Ellipse, finalSize: Size) -> Size """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """ MeasureOverride(self: Ellipse, constraint: Size) -> Size """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """ OnRender(self: Ellipse, drawingContext: DrawingContext) """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GeometryTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value of any System.Windows.Media.Transform.Identity transforms that are applied to the System.Windows.Media.Geometry of an System.Windows.Shapes.Ellipse before it is rendered.

Get: GeometryTransform(self: Ellipse) -> Transform

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    RenderedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the final rendered System.Windows.Media.Geometry of an System.Windows.Shapes.Ellipse.

Get: RenderedGeometry(self: Ellipse) -> Geometry

"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""



class Line(Shape, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Draws a straight line between two points.
    
    Line()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Shape, finalSize: Size) -> Size
        
            Arranges a System.Windows.Shapes.Shape by evaluating its 
             System.Windows.Shapes.Shape.RenderedGeometry and 
             System.Windows.Shapes.Shape.Stretch properties.
        
        
            finalSize: The final evaluated size of the System.Windows.Shapes.Shape.
            Returns: The final size of the arranged System.Windows.Shapes.Shape element.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Shape, constraint: Size) -> Size
        
            Measures a System.Windows.Shapes.Shape during the first layout pass prior to 
             arranging it.
        
        
            constraint: A maximum System.Windows.Size to not exceed.
            Returns: The maximum System.Windows.Size for the System.Windows.Shapes.Shape.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: Shape, drawingContext: DrawingContext)
            Provides a means to change the default appearance of a 
             System.Windows.Shapes.Shape element.
        
        
            drawingContext: A System.Windows.Media.DrawingContext object that is drawn during the rendering 
             pass of this System.Windows.Shapes.Shape.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""

    X1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the System.Windows.Shapes.Line start point.

Get: X1(self: Line) -> float

Set: X1(self: Line) = value
"""

    X2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the System.Windows.Shapes.Line end point.

Get: X2(self: Line) -> float

Set: X2(self: Line) = value
"""

    Y1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the System.Windows.Shapes.Line start point.

Get: Y1(self: Line) -> float

Set: Y1(self: Line) = value
"""

    Y2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the System.Windows.Shapes.Line end point.

Get: Y2(self: Line) -> float

Set: Y2(self: Line) = value
"""


    X1Property = None
    X2Property = None
    Y1Property = None
    Y2Property = None


class Path(Shape, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Draws a series of connected lines and curves.
    
    Path()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Shape, finalSize: Size) -> Size
        
            Arranges a System.Windows.Shapes.Shape by evaluating its 
             System.Windows.Shapes.Shape.RenderedGeometry and 
             System.Windows.Shapes.Shape.Stretch properties.
        
        
            finalSize: The final evaluated size of the System.Windows.Shapes.Shape.
            Returns: The final size of the arranged System.Windows.Shapes.Shape element.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Shape, constraint: Size) -> Size
        
            Measures a System.Windows.Shapes.Shape during the first layout pass prior to 
             arranging it.
        
        
            constraint: A maximum System.Windows.Size to not exceed.
            Returns: The maximum System.Windows.Size for the System.Windows.Shapes.Shape.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: Shape, drawingContext: DrawingContext)
            Provides a means to change the default appearance of a 
             System.Windows.Shapes.Shape element.
        
        
            drawingContext: A System.Windows.Media.DrawingContext object that is drawn during the rendering 
             pass of this System.Windows.Shapes.Shape.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.Geometry that specifies the shape to be drawn.

Get: Data(self: Path) -> Geometry

Set: Data(self: Path) = value
"""

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


    DataProperty = None


class Polygon(Shape, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Draws a polygon, which is a connected series of lines that form a closed shape.
    
    Polygon()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Shape, finalSize: Size) -> Size
        
            Arranges a System.Windows.Shapes.Shape by evaluating its 
             System.Windows.Shapes.Shape.RenderedGeometry and 
             System.Windows.Shapes.Shape.Stretch properties.
        
        
            finalSize: The final evaluated size of the System.Windows.Shapes.Shape.
            Returns: The final size of the arranged System.Windows.Shapes.Shape element.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Shape, constraint: Size) -> Size
        
            Measures a System.Windows.Shapes.Shape during the first layout pass prior to 
             arranging it.
        
        
            constraint: A maximum System.Windows.Size to not exceed.
            Returns: The maximum System.Windows.Size for the System.Windows.Shapes.Shape.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: Shape, drawingContext: DrawingContext)
            Provides a means to change the default appearance of a 
             System.Windows.Shapes.Shape element.
        
        
            drawingContext: A System.Windows.Media.DrawingContext object that is drawn during the rendering 
             pass of this System.Windows.Shapes.Shape.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FillRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.FillRule enumeration that specifies how the interior fill of the shape is determined.

Get: FillRule(self: Polygon) -> FillRule

Set: FillRule(self: Polygon) = value
"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a collection that contains the vertex points of the polygon.

Get: Points(self: Polygon) -> PointCollection

Set: Points(self: Polygon) = value
"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


    FillRuleProperty = None
    PointsProperty = None


class Polyline(Shape, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Draws a series of connected straight lines.
    
    Polyline()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Shape, finalSize: Size) -> Size
        
            Arranges a System.Windows.Shapes.Shape by evaluating its 
             System.Windows.Shapes.Shape.RenderedGeometry and 
             System.Windows.Shapes.Shape.Stretch properties.
        
        
            finalSize: The final evaluated size of the System.Windows.Shapes.Shape.
            Returns: The final size of the arranged System.Windows.Shapes.Shape element.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Shape, constraint: Size) -> Size
        
            Measures a System.Windows.Shapes.Shape during the first layout pass prior to 
             arranging it.
        
        
            constraint: A maximum System.Windows.Size to not exceed.
            Returns: The maximum System.Windows.Size for the System.Windows.Shapes.Shape.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: Shape, drawingContext: DrawingContext)
            Provides a means to change the default appearance of a 
             System.Windows.Shapes.Shape element.
        
        
            drawingContext: A System.Windows.Media.DrawingContext object that is drawn during the rendering 
             pass of this System.Windows.Shapes.Shape.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FillRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Windows.Media.FillRule enumeration that specifies how the interior fill of the shape is determined.

Get: FillRule(self: Polyline) -> FillRule

Set: FillRule(self: Polyline) = value
"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a collection that contains the vertex points of the System.Windows.Shapes.Polyline.

Get: Points(self: Polyline) -> PointCollection

Set: Points(self: Polyline) = value
"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


    FillRuleProperty = None
    PointsProperty = None


class Rectangle(Shape, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Draws a rectangle.
    
    Rectangle()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        AddLogicalChild(self: Window_16$17, child: object)AddLogicalChild(self: Label_17$18, child: object)AddLogicalChild(self: TextBox_18$19, child: object)AddLogicalChild(self: Button_19$20, child: object)AddLogicalChild(self: CheckBox_20$21, child: object)AddLogicalChild(self: ComboBox_21$22, child: object)AddLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        AddVisualChild(self: Window_16$17, child: Window_16$17)AddVisualChild(self: Label_17$18, child: Label_17$18)AddVisualChild(self: TextBox_18$19, child: TextBox_18$19)AddVisualChild(self: Button_19$20, child: Button_19$20)AddVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)AddVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)AddVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined 
             as virtual in System.Windows.UIElement) and seals the implementation.
        
        
            finalRect: The final area within the parent that this element should use to arrange itself 
             and its children.
        
        ArrangeCore(self: Window_16$17, finalRect: Rect)ArrangeCore(self: Label_17$18, finalRect: Rect)ArrangeCore(self: TextBox_18$19, finalRect: Rect)ArrangeCore(self: Button_19$20, finalRect: Rect)ArrangeCore(self: CheckBox_20$21, finalRect: Rect)ArrangeCore(self: ComboBox_21$22, finalRect: Rect)ArrangeCore(self: Separator_22$23, finalRect: Rect)
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """ ArrangeOverride(self: Rectangle, finalSize: Size) -> Size """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system 
             attempts to arrange an element that is larger than the available display space.
        
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        GetLayoutClip(self: Window_16$17, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Label_17$18, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: TextBox_18$19, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Button_19$20, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: CheckBox_20$21, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: ComboBox_21$22, layoutSlotSize: Size) -> Geometry
        GetLayoutClip(self: Separator_22$23, layoutSlotSize: Size) -> Geometry
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated 
             System.Windows.Controls.ControlTemplate.
        
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        GetTemplateChild(self: Window_16$17, childName: str) -> DependencyObject
        GetTemplateChild(self: Label_17$18, childName: str) -> DependencyObject
        GetTemplateChild(self: TextBox_18$19, childName: str) -> DependencyObject
        GetTemplateChild(self: Button_19$20, childName: str) -> DependencyObject
        GetTemplateChild(self: CheckBox_20$21, childName: str) -> DependencyObject
        GetTemplateChild(self: ComboBox_21$22, childName: str) -> DependencyObject
        GetTemplateChild(self: Separator_22$23, childName: str) -> DependencyObject
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual 
             parent.
        
            Returns: Returns something other than null whenever a WPF framework-level implementation 
             of this method has a non-visual parent connection.
        
        GetUIParentCore(self: Window_16$17) -> DependencyObject
        GetUIParentCore(self: Label_17$18) -> DependencyObject
        GetUIParentCore(self: TextBox_18$19) -> DependencyObject
        GetUIParentCore(self: Button_19$20) -> DependencyObject
        GetUIParentCore(self: CheckBox_20$21) -> DependencyObject
        GetUIParentCore(self: ComboBox_21$22) -> DependencyObject
        GetUIParentCore(self: Separator_22$23) -> DependencyObject
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns 
             a child at the specified index from a collection of child elements.
        
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index 
             is out of range, an exception is thrown.
        
        GetVisualChild(self: Window_16$17, index: int) -> Visual
        GetVisualChild(self: Label_17$18, index: int) -> Visual
        GetVisualChild(self: TextBox_18$19, index: int) -> Visual
        GetVisualChild(self: Button_19$20, index: int) -> Visual
        GetVisualChild(self: CheckBox_20$21, index: int) -> Visual
        GetVisualChild(self: ComboBox_21$22, index: int) -> Visual
        GetVisualChild(self: Separator_22$23, index: int) -> Visual
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestPara
             meters) to supply base element hit testing behavior (returning 
             System.Windows.Media.GeometryHitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements 
             System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParamet
             ers) to supply base element hit testing behavior (returning 
             System.Windows.Media.HitTestResult).
        
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        HitTestCore(self: Window_16$17, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Window_16$17, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Label_17$18, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: TextBox_18$19, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Button_19$20, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: CheckBox_20$21, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: ComboBox_21$22, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: PointHitTestParameters) -> HitTestResult
        HitTestCore(self: Separator_22$23, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for 
             System.Windows.FrameworkElement.
        
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        MeasureCore(self: Window_16$17, availableSize: Size) -> Size
        MeasureCore(self: Label_17$18, availableSize: Size) -> Size
        MeasureCore(self: TextBox_18$19, availableSize: Size) -> Size
        MeasureCore(self: Button_19$20, availableSize: Size) -> Size
        MeasureCore(self: CheckBox_20$21, availableSize: Size) -> Size
        MeasureCore(self: ComboBox_21$22, availableSize: Size) -> Size
        MeasureCore(self: Separator_22$23, availableSize: Size) -> Size
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """ MeasureOverride(self: Rectangle, constraint: Size) -> Size """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this 
             element is invoked.
        
        
            e: The event data to the access key event. The event data reports which key was 
             invoked, and indicate whether the System.Windows.Input.AccessKeyManager object 
             that controls the sending of these events also sent this access key invocation 
             to other elements.
        
        OnAccessKey(self: Window_16$17, e: AccessKeyEventArgs)OnAccessKey(self: Label_17$18, e: AccessKeyEventArgs)OnAccessKey(self: TextBox_18$19, e: AccessKeyEventArgs)OnAccessKey(self: Button_19$20, e: AccessKeyEventArgs)OnAccessKey(self: CheckBox_20$21, e: AccessKeyEventArgs)OnAccessKey(self: ComboBox_21$22, e: AccessKeyEventArgs)OnAccessKey(self: Separator_22$23, e: AccessKeyEventArgs)
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        OnChildDesiredSizeChanged(self: Window_16$17, child: Window_16$17)OnChildDesiredSizeChanged(self: Label_17$18, child: Label_17$18)OnChildDesiredSizeChanged(self: TextBox_18$19, child: TextBox_18$19)OnChildDesiredSizeChanged(self: Button_19$20, child: Button_19$20)OnChildDesiredSizeChanged(self: CheckBox_20$21, child: CheckBox_20$21)OnChildDesiredSizeChanged(self: ComboBox_21$22, child: ComboBox_21$22)OnChildDesiredSizeChanged(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: Provides data about the event.
        OnContextMenuClosing(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuClosing(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuClosing(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuClosing(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuClosing(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuClosing(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuClosing(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled 
             System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this 
             class in its route. Implement this method to add class handling for this event.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnContextMenuOpening(self: Window_16$17, e: ContextMenuEventArgs)OnContextMenuOpening(self: Label_17$18, e: ContextMenuEventArgs)OnContextMenuOpening(self: TextBox_18$19, e: ContextMenuEventArgs)OnContextMenuOpening(self: Button_19$20, e: ContextMenuEventArgs)OnContextMenuOpening(self: CheckBox_20$21, e: ContextMenuEventArgs)OnContextMenuOpening(self: ComboBox_21$22, e: ContextMenuEventArgs)OnContextMenuOpening(self: Separator_22$23, e: ContextMenuEventArgs)
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: UIElement) -> AutomationPeer
        
            Returns class-specific System.Windows.Automation.Peers.AutomationPeer 
             implementations for the Windows Presentation Foundation (WPF) infrastructure.
        
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        OnCreateAutomationPeer(self: Window_16$17) -> AutomationPeer
        OnCreateAutomationPeer(self: Label_17$18) -> AutomationPeer
        OnCreateAutomationPeer(self: TextBox_18$19) -> AutomationPeer
        OnCreateAutomationPeer(self: Button_19$20) -> AutomationPeer
        OnCreateAutomationPeer(self: CheckBox_20$21) -> AutomationPeer
        OnCreateAutomationPeer(self: ComboBox_21$22) -> AutomationPeer
        OnCreateAutomationPeer(self: Separator_22$23) -> AutomationPeer
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Window_16$17, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Label_17$18, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: TextBox_18$19, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Button_19$20, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: CheckBox_20$21, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: ComboBox_21$22, oldDpi: DpiScale, newDpi: DpiScale)OnDpiChanged(self: Separator_22$23, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragEnter(self: Window_16$17, e: DragEventArgs)OnDragEnter(self: Label_17$18, e: DragEventArgs)OnDragEnter(self: TextBox_18$19, e: DragEventArgs)OnDragEnter(self: Button_19$20, e: DragEventArgs)OnDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragLeave(self: Window_16$17, e: DragEventArgs)OnDragLeave(self: Label_17$18, e: DragEventArgs)OnDragLeave(self: TextBox_18$19, e: DragEventArgs)OnDragLeave(self: Button_19$20, e: DragEventArgs)OnDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDragOver(self: Window_16$17, e: DragEventArgs)OnDragOver(self: Label_17$18, e: DragEventArgs)OnDragOver(self: TextBox_18$19, e: DragEventArgs)OnDragOver(self: Button_19$20, e: DragEventArgs)OnDragOver(self: CheckBox_20$21, e: DragEventArgs)OnDragOver(self: ComboBox_21$22, e: DragEventArgs)OnDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnDrop(self: Window_16$17, e: DragEventArgs)OnDrop(self: Label_17$18, e: DragEventArgs)OnDrop(self: TextBox_18$19, e: DragEventArgs)OnDrop(self: Button_19$20, e: DragEventArgs)OnDrop(self: CheckBox_20$21, e: DragEventArgs)OnDrop(self: ComboBox_21$22, e: DragEventArgs)OnDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches 
             this element in its route.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnGotFocus(self: Window_16$17, e: RoutedEventArgs)OnGotFocus(self: Label_17$18, e: RoutedEventArgs)OnGotFocus(self: TextBox_18$19, e: RoutedEventArgs)OnGotFocus(self: Button_19$20, e: RoutedEventArgs)OnGotFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnGotFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnGotMouseCapture(self: Window_16$17, e: MouseEventArgs)OnGotMouseCapture(self: Label_17$18, e: MouseEventArgs)OnGotMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnGotMouseCapture(self: Button_19$20, e: MouseEventArgs)OnGotMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnGotMouseCapture(self: ComboBox_21$22, e: MouseEventArgs)OnGotMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnGotStylusCapture(self: Window_16$17, e: StylusEventArgs)OnGotStylusCapture(self: Label_17$18, e: StylusEventArgs)OnGotStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnGotStylusCapture(self: Button_19$20, e: StylusEventArgs)OnGotStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnGotStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnGotStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed 
             event that occurs when a touch is captured to this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnGotTouchCapture(self: Window_16$17, e: TouchEventArgs)OnGotTouchCapture(self: Label_17$18, e: TouchEventArgs)OnGotTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnGotTouchCapture(self: Button_19$20, e: TouchEventArgs)OnGotTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnGotTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnGotTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is 
             invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true 
             internally.
        
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        OnInitialized(self: Window_16$17, e: EventArgs)OnInitialized(self: Label_17$18, e: EventArgs)OnInitialized(self: TextBox_18$19, e: EventArgs)OnInitialized(self: Button_19$20, e: EventArgs)OnInitialized(self: CheckBox_20$21, e: EventArgs)OnInitialized(self: ComboBox_21$22, e: EventArgs)OnInitialized(self: Separator_22$23, e: EventArgs)
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsKeyboardFocusWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsKeyboardFocusWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsMouseDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsMouseDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCapturedChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCapturedChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusCaptureWithinChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusCaptureWithinChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event 
             data.
        
        OnIsStylusDirectlyOverChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnIsStylusDirectlyOverChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyDown(self: Window_16$17, e: KeyEventArgs)OnKeyDown(self: Label_17$18, e: KeyEventArgs)OnKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnKeyDown(self: Button_19$20, e: KeyEventArgs)OnKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnKeyUp(self: Window_16$17, e: KeyEventArgs)OnKeyUp(self: Label_17$18, e: KeyEventArgs)OnKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnKeyUp(self: Button_19$20, e: KeyEventArgs)OnKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event 
             data that is provided.
        
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must 
             contain the identifier for the System.Windows.UIElement.LostFocus event.
        
        OnLostFocus(self: Window_16$17, e: RoutedEventArgs)OnLostFocus(self: Label_17$18, e: RoutedEventArgs)OnLostFocus(self: TextBox_18$19, e: RoutedEventArgs)OnLostFocus(self: Button_19$20, e: RoutedEventArgs)OnLostFocus(self: CheckBox_20$21, e: RoutedEventArgs)OnLostFocus(self: ComboBox_21$22, e: RoutedEventArgs)OnLostFocus(self: Separator_22$23, e: RoutedEventArgs)
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        OnLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        OnLostMouseCapture(self: Window_16$17, e: MouseEventArgs)OnLostMouseCapture(self: Label_17$18, e: MouseEventArgs)OnLostMouseCapture(self: TextBox_18$19, e: MouseEventArgs)OnLostMouseCapture(self: Button_19$20, e: MouseEventArgs)OnLostMouseCapture(self: CheckBox_20$21, e: MouseEventArgs)OnLostMouseCapture(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        OnLostStylusCapture(self: Window_16$17, e: StylusEventArgs)OnLostStylusCapture(self: Label_17$18, e: StylusEventArgs)OnLostStylusCapture(self: TextBox_18$19, e: StylusEventArgs)OnLostStylusCapture(self: Button_19$20, e: StylusEventArgs)OnLostStylusCapture(self: CheckBox_20$21, e: StylusEventArgs)OnLostStylusCapture(self: ComboBox_21$22, e: StylusEventArgs)OnLostStylusCapture(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture 
             routed event that occurs when this element loses a touch capture.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnLostTouchCapture(self: Window_16$17, e: TouchEventArgs)OnLostTouchCapture(self: Label_17$18, e: TouchEventArgs)OnLostTouchCapture(self: TextBox_18$19, e: TouchEventArgs)OnLostTouchCapture(self: Button_19$20, e: TouchEventArgs)OnLostTouchCapture(self: CheckBox_20$21, e: TouchEventArgs)OnLostTouchCapture(self: ComboBox_21$22, e: TouchEventArgs)OnLostTouchCapture(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationBoundaryFeedback(self: Window_16$17, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Label_17$18, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: TextBox_18$19, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Button_19$20, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: CheckBox_20$21, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: ComboBox_21$22, e: ManipulationBoundaryFeedbackEventArgs)OnManipulationBoundaryFeedback(self: Separator_22$23, e: ManipulationBoundaryFeedbackEventArgs)
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        OnManipulationCompleted(self: Window_16$17, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Label_17$18, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: TextBox_18$19, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Button_19$20, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: CheckBox_20$21, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: ComboBox_21$22, e: ManipulationCompletedEventArgs)OnManipulationCompleted(self: Separator_22$23, e: ManipulationCompletedEventArgs)
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        OnManipulationDelta(self: Window_16$17, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Label_17$18, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: TextBox_18$19, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Button_19$20, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: CheckBox_20$21, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: ComboBox_21$22, e: ManipulationDeltaEventArgs)OnManipulationDelta(self: Separator_22$23, e: ManipulationDeltaEventArgs)
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event 
             occurs.
        
        
            e: The data for the event.
        OnManipulationInertiaStarting(self: Window_16$17, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Label_17$18, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: TextBox_18$19, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Button_19$20, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: CheckBox_20$21, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: ComboBox_21$22, e: ManipulationInertiaStartingEventArgs)OnManipulationInertiaStarting(self: Separator_22$23, e: ManipulationInertiaStartingEventArgs)
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        OnManipulationStarted(self: Window_16$17, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Label_17$18, e: ManipulationStartedEventArgs)OnManipulationStarted(self: TextBox_18$19, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Button_19$20, e: ManipulationStartedEventArgs)OnManipulationStarted(self: CheckBox_20$21, e: ManipulationStartedEventArgs)OnManipulationStarted(self: ComboBox_21$22, e: ManipulationStartedEventArgs)OnManipulationStarted(self: Separator_22$23, e: ManipulationStartedEventArgs)
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting 
             routed event that occurs when the manipulation processor is first created.
        
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event 
             data.
        
        OnManipulationStarting(self: Window_16$17, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Label_17$18, e: ManipulationStartingEventArgs)OnManipulationStarting(self: TextBox_18$19, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Button_19$20, e: ManipulationStartingEventArgs)OnManipulationStarting(self: CheckBox_20$21, e: ManipulationStartingEventArgs)OnManipulationStarting(self: ComboBox_21$22, e: ManipulationStartingEventArgs)OnManipulationStarting(self: Separator_22$23, e: ManipulationStartingEventArgs)
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. 
             This event data reports details about the mouse button that was pressed and the 
             handled state.
        
        OnMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseEnter(self: Window_16$17, e: MouseEventArgs)OnMouseEnter(self: Label_17$18, e: MouseEventArgs)OnMouseEnter(self: TextBox_18$19, e: MouseEventArgs)OnMouseEnter(self: Button_19$20, e: MouseEventArgs)OnMouseEnter(self: CheckBox_20$21, e: MouseEventArgs)OnMouseEnter(self: ComboBox_21$22, e: MouseEventArgs)OnMouseEnter(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event 
             is raised on this element. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseLeave(self: Window_16$17, e: MouseEventArgs)OnMouseLeave(self: Label_17$18, e: MouseEventArgs)OnMouseLeave(self: TextBox_18$19, e: MouseEventArgs)OnMouseLeave(self: Button_19$20, e: MouseEventArgs)OnMouseLeave(self: CheckBox_20$21, e: MouseEventArgs)OnMouseLeave(self: ComboBox_21$22, e: MouseEventArgs)OnMouseLeave(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed 
             event is raised on this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnMouseMove(self: Window_16$17, e: MouseEventArgs)OnMouseMove(self: Label_17$18, e: MouseEventArgs)OnMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnMouseMove(self: Button_19$20, e: MouseEventArgs)OnMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the mouse button was released.
        
        OnMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragEnter(self: Window_16$17, e: DragEventArgs)OnPreviewDragEnter(self: Label_17$18, e: DragEventArgs)OnPreviewDragEnter(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragEnter(self: Button_19$20, e: DragEventArgs)OnPreviewDragEnter(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragEnter(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragEnter(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragLeave(self: Window_16$17, e: DragEventArgs)OnPreviewDragLeave(self: Label_17$18, e: DragEventArgs)OnPreviewDragLeave(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragLeave(self: Button_19$20, e: DragEventArgs)OnPreviewDragLeave(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragLeave(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragLeave(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDragOver(self: Window_16$17, e: DragEventArgs)OnPreviewDragOver(self: Label_17$18, e: DragEventArgs)OnPreviewDragOver(self: TextBox_18$19, e: DragEventArgs)OnPreviewDragOver(self: Button_19$20, e: DragEventArgs)OnPreviewDragOver(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDragOver(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDragOver(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.DragEventArgs that contains the event data.
        OnPreviewDrop(self: Window_16$17, e: DragEventArgs)OnPreviewDrop(self: Label_17$18, e: DragEventArgs)OnPreviewDrop(self: TextBox_18$19, e: DragEventArgs)OnPreviewDrop(self: Button_19$20, e: DragEventArgs)OnPreviewDrop(self: CheckBox_20$21, e: DragEventArgs)OnPreviewDrop(self: ComboBox_21$22, e: DragEventArgs)OnPreviewDrop(self: Separator_22$23, e: DragEventArgs)
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        OnPreviewGiveFeedback(self: Window_16$17, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Label_17$18, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: TextBox_18$19, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Button_19$20, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: CheckBox_20$21, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: ComboBox_21$22, e: GiveFeedbackEventArgs)OnPreviewGiveFeedback(self: Separator_22$23, e: GiveFeedbackEventArgs)
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewGotKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewGotKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyDown(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyDown(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyDown(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyDown(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyDown(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyDown(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyDown(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        OnPreviewKeyUp(self: Window_16$17, e: KeyEventArgs)OnPreviewKeyUp(self: Label_17$18, e: KeyEventArgs)OnPreviewKeyUp(self: TextBox_18$19, e: KeyEventArgs)OnPreviewKeyUp(self: Button_19$20, e: KeyEventArgs)OnPreviewKeyUp(self: CheckBox_20$21, e: KeyEventArgs)OnPreviewKeyUp(self: ComboBox_21$22, e: KeyEventArgs)OnPreviewKeyUp(self: Separator_22$23, e: KeyEventArgs)
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event 
             data.
        
        OnPreviewLostKeyboardFocus(self: Window_16$17, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Label_17$18, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: TextBox_18$19, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Button_19$20, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: CheckBox_20$21, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: ComboBox_21$22, e: KeyboardFocusChangedEventArgs)OnPreviewLostKeyboardFocus(self: Separator_22$23, e: KeyboardFocusChangedEventArgs)
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were pressed.
        
        OnPreviewMouseDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was pressed.
        
        OnPreviewMouseLeftButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the left mouse button was released.
        
        OnPreviewMouseLeftButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseLeftButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        OnPreviewMouseMove(self: Window_16$17, e: MouseEventArgs)OnPreviewMouseMove(self: Label_17$18, e: MouseEventArgs)OnPreviewMouseMove(self: TextBox_18$19, e: MouseEventArgs)OnPreviewMouseMove(self: Button_19$20, e: MouseEventArgs)OnPreviewMouseMove(self: CheckBox_20$21, e: MouseEventArgs)OnPreviewMouseMove(self: ComboBox_21$22, e: MouseEventArgs)OnPreviewMouseMove(self: Separator_22$23, e: MouseEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was pressed.
        
        OnPreviewMouseRightButtonDown(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonDown(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�
             routed event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that the right mouse button was released.
        
        OnPreviewMouseRightButtonUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseRightButtonUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The 
             event data reports that one or more mouse buttons were released.
        
        OnPreviewMouseUp(self: Window_16$17, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Label_17$18, e: MouseButtonEventArgs)OnPreviewMouseUp(self: TextBox_18$19, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Button_19$20, e: MouseButtonEventArgs)OnPreviewMouseUp(self: CheckBox_20$21, e: MouseButtonEventArgs)OnPreviewMouseUp(self: ComboBox_21$22, e: MouseButtonEventArgs)OnPreviewMouseUp(self: Separator_22$23, e: MouseButtonEventArgs)
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        OnPreviewMouseWheel(self: Window_16$17, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Label_17$18, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: TextBox_18$19, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Button_19$20, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: CheckBox_20$21, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: ComboBox_21$22, e: MouseWheelEventArgs)OnPreviewMouseWheel(self: Separator_22$23, e: MouseWheelEventArgs)
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnPreviewQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnPreviewQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnPreviewStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnPreviewStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnPreviewStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnPreviewStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnPreviewStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnPreviewStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnPreviewStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnPreviewStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnPreviewStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusInRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusInRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusInRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusMove(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusMove(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusMove(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches 
             an element in its route that is derived from this class. Implement this method 
             to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnPreviewStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnPreviewStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnPreviewStylusUp(self: Window_16$17, e: StylusEventArgs)OnPreviewStylusUp(self: Label_17$18, e: StylusEventArgs)OnPreviewStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnPreviewStylusUp(self: Button_19$20, e: StylusEventArgs)OnPreviewStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnPreviewStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnPreviewStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled 
             System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnPreviewTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnPreviewTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnPreviewTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnPreviewTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnPreviewTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnPreviewTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnPreviewTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown 
             routed event that occurs when a touch presses this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchDown(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchDown(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchDown(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove 
             routed event that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchMove(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchMove(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchMove(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed 
             event that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnPreviewTouchUp(self: Window_16$17, e: TouchEventArgs)OnPreviewTouchUp(self: Label_17$18, e: TouchEventArgs)OnPreviewTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnPreviewTouchUp(self: Button_19$20, e: TouchEventArgs)OnPreviewTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnPreviewTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnPreviewTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this 
             System.Windows.FrameworkElement has been updated. The specific dependency 
             property that changed is reported in the arguments parameter. Overrides 
             System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPrope
             rtyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new 
             values.
        
        OnPropertyChanged(self: Window_16$17, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Label_17$18, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: TextBox_18$19, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Button_19$20, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: CheckBox_20$21, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: ComboBox_21$22, e: DependencyPropertyChangedEventArgs)OnPropertyChanged(self: Separator_22$23, e: DependencyPropertyChangedEventArgs)
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        OnQueryContinueDrag(self: Window_16$17, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Label_17$18, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: TextBox_18$19, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Button_19$20, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: CheckBox_20$21, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: ComboBox_21$22, e: QueryContinueDragEventArgs)OnQueryContinueDrag(self: Separator_22$23, e: QueryContinueDragEventArgs)
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        OnQueryCursor(self: Window_16$17, e: QueryCursorEventArgs)OnQueryCursor(self: Label_17$18, e: QueryCursorEventArgs)OnQueryCursor(self: TextBox_18$19, e: QueryCursorEventArgs)OnQueryCursor(self: Button_19$20, e: QueryCursorEventArgs)OnQueryCursor(self: CheckBox_20$21, e: QueryCursorEventArgs)OnQueryCursor(self: ComboBox_21$22, e: QueryCursorEventArgs)OnQueryCursor(self: Separator_22$23, e: QueryCursorEventArgs)
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """ OnRender(self: Rectangle, drawingContext: DrawingContext) """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the 
             specified information as part of the eventual event data.
        
        
            sizeInfo: Details of the old and new size involved in the change.
        OnRenderSizeChanged(self: Window_16$17, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Label_17$18, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: TextBox_18$19, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Button_19$20, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: CheckBox_20$21, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: ComboBox_21$22, sizeInfo: SizeChangedInfo)OnRenderSizeChanged(self: Separator_22$23, sizeInfo: SizeChangedInfo)
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate 
             the layout.
        
        
            oldStyle: The old style.
            newStyle: The new style.
        OnStyleChanged(self: Window_16$17, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Label_17$18, oldStyle: Style, newStyle: Style)OnStyleChanged(self: TextBox_18$19, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Button_19$20, oldStyle: Style, newStyle: Style)OnStyleChanged(self: CheckBox_20$21, oldStyle: Style, newStyle: Style)OnStyleChanged(self: ComboBox_21$22, oldStyle: Style, newStyle: Style)OnStyleChanged(self: Separator_22$23, oldStyle: Style, newStyle: Style)
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonDown(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonDown(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonDown(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonDown(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonDown(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonDown(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonDown(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        OnStylusButtonUp(self: Window_16$17, e: StylusButtonEventArgs)OnStylusButtonUp(self: Label_17$18, e: StylusButtonEventArgs)OnStylusButtonUp(self: TextBox_18$19, e: StylusButtonEventArgs)OnStylusButtonUp(self: Button_19$20, e: StylusButtonEventArgs)OnStylusButtonUp(self: CheckBox_20$21, e: StylusButtonEventArgs)OnStylusButtonUp(self: ComboBox_21$22, e: StylusButtonEventArgs)OnStylusButtonUp(self: Separator_22$23, e: StylusButtonEventArgs)
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        OnStylusDown(self: Window_16$17, e: StylusDownEventArgs)OnStylusDown(self: Label_17$18, e: StylusDownEventArgs)OnStylusDown(self: TextBox_18$19, e: StylusDownEventArgs)OnStylusDown(self: Button_19$20, e: StylusDownEventArgs)OnStylusDown(self: CheckBox_20$21, e: StylusDownEventArgs)OnStylusDown(self: ComboBox_21$22, e: StylusDownEventArgs)OnStylusDown(self: Separator_22$23, e: StylusDownEventArgs)
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusEnter(self: Window_16$17, e: StylusEventArgs)OnStylusEnter(self: Label_17$18, e: StylusEventArgs)OnStylusEnter(self: TextBox_18$19, e: StylusEventArgs)OnStylusEnter(self: Button_19$20, e: StylusEventArgs)OnStylusEnter(self: CheckBox_20$21, e: StylusEventArgs)OnStylusEnter(self: ComboBox_21$22, e: StylusEventArgs)OnStylusEnter(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInAirMove(self: Window_16$17, e: StylusEventArgs)OnStylusInAirMove(self: Label_17$18, e: StylusEventArgs)OnStylusInAirMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusInAirMove(self: Button_19$20, e: StylusEventArgs)OnStylusInAirMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInAirMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInAirMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusInRange(self: Window_16$17, e: StylusEventArgs)OnStylusInRange(self: Label_17$18, e: StylusEventArgs)OnStylusInRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusInRange(self: Button_19$20, e: StylusEventArgs)OnStylusInRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusInRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusInRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached 
             event is raised by this element. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusLeave(self: Window_16$17, e: StylusEventArgs)OnStylusLeave(self: Label_17$18, e: StylusEventArgs)OnStylusLeave(self: TextBox_18$19, e: StylusEventArgs)OnStylusLeave(self: Button_19$20, e: StylusEventArgs)OnStylusLeave(self: CheckBox_20$21, e: StylusEventArgs)OnStylusLeave(self: ComboBox_21$22, e: StylusEventArgs)OnStylusLeave(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusMove(self: Window_16$17, e: StylusEventArgs)OnStylusMove(self: Label_17$18, e: StylusEventArgs)OnStylusMove(self: TextBox_18$19, e: StylusEventArgs)OnStylusMove(self: Button_19$20, e: StylusEventArgs)OnStylusMove(self: CheckBox_20$21, e: StylusEventArgs)OnStylusMove(self: ComboBox_21$22, e: StylusEventArgs)OnStylusMove(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached 
             event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusOutOfRange(self: Window_16$17, e: StylusEventArgs)OnStylusOutOfRange(self: Label_17$18, e: StylusEventArgs)OnStylusOutOfRange(self: TextBox_18$19, e: StylusEventArgs)OnStylusOutOfRange(self: Button_19$20, e: StylusEventArgs)OnStylusOutOfRange(self: CheckBox_20$21, e: StylusEventArgs)OnStylusOutOfRange(self: ComboBox_21$22, e: StylusEventArgs)OnStylusOutOfRange(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event 
             data.
        
        OnStylusSystemGesture(self: Window_16$17, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Label_17$18, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: TextBox_18$19, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Button_19$20, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: CheckBox_20$21, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: ComboBox_21$22, e: StylusSystemGestureEventArgs)OnStylusSystemGesture(self: Separator_22$23, e: StylusSystemGestureEventArgs)
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event 
             reaches an element in its route that is derived from this class. Implement this 
             method to add class handling for this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        OnStylusUp(self: Window_16$17, e: StylusEventArgs)OnStylusUp(self: Label_17$18, e: StylusEventArgs)OnStylusUp(self: TextBox_18$19, e: StylusEventArgs)OnStylusUp(self: Button_19$20, e: StylusEventArgs)OnStylusUp(self: CheckBox_20$21, e: StylusEventArgs)OnStylusUp(self: ComboBox_21$22, e: StylusEventArgs)OnStylusUp(self: Separator_22$23, e: StylusEventArgs)
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�
             attached event reaches an element in its route that is derived from this class. 
             Implement this method to add class handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        OnTextInput(self: Window_16$17, e: TextCompositionEventArgs)OnTextInput(self: Label_17$18, e: TextCompositionEventArgs)OnTextInput(self: TextBox_18$19, e: TextCompositionEventArgs)OnTextInput(self: Button_19$20, e: TextCompositionEventArgs)OnTextInput(self: CheckBox_20$21, e: TextCompositionEventArgs)OnTextInput(self: ComboBox_21$22, e: TextCompositionEventArgs)OnTextInput(self: Separator_22$23, e: TextCompositionEventArgs)
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing 
             routed event reaches this class in its route. Implement this method to add 
             class handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipClosing(self: Window_16$17, e: ToolTipEventArgs)OnToolTipClosing(self: Label_17$18, e: ToolTipEventArgs)OnToolTipClosing(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipClosing(self: Button_19$20, e: ToolTipEventArgs)OnToolTipClosing(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipClosing(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipClosing(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed 
             event reaches this class in its route. Implement this method to add class 
             handling for this event.
        
        
            e: Provides data about the event.
        OnToolTipOpening(self: Window_16$17, e: ToolTipEventArgs)OnToolTipOpening(self: Label_17$18, e: ToolTipEventArgs)OnToolTipOpening(self: TextBox_18$19, e: ToolTipEventArgs)OnToolTipOpening(self: Button_19$20, e: ToolTipEventArgs)OnToolTipOpening(self: CheckBox_20$21, e: ToolTipEventArgs)OnToolTipOpening(self: ComboBox_21$22, e: ToolTipEventArgs)OnToolTipOpening(self: Separator_22$23, e: ToolTipEventArgs)
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event 
             that occurs when a touch presses inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchDown(self: Window_16$17, e: TouchEventArgs)OnTouchDown(self: Label_17$18, e: TouchEventArgs)OnTouchDown(self: TextBox_18$19, e: TouchEventArgs)OnTouchDown(self: Button_19$20, e: TouchEventArgs)OnTouchDown(self: CheckBox_20$21, e: TouchEventArgs)OnTouchDown(self: ComboBox_21$22, e: TouchEventArgs)OnTouchDown(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed 
             event that occurs when a touch moves from outside to inside the bounds of this 
             element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchEnter(self: Window_16$17, e: TouchEventArgs)OnTouchEnter(self: Label_17$18, e: TouchEventArgs)OnTouchEnter(self: TextBox_18$19, e: TouchEventArgs)OnTouchEnter(self: Button_19$20, e: TouchEventArgs)OnTouchEnter(self: CheckBox_20$21, e: TouchEventArgs)OnTouchEnter(self: ComboBox_21$22, e: TouchEventArgs)OnTouchEnter(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed 
             event that occurs when a touch moves from inside to outside the bounds of this 
             System.Windows.UIElement.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchLeave(self: Window_16$17, e: TouchEventArgs)OnTouchLeave(self: Label_17$18, e: TouchEventArgs)OnTouchLeave(self: TextBox_18$19, e: TouchEventArgs)OnTouchLeave(self: Button_19$20, e: TouchEventArgs)OnTouchLeave(self: CheckBox_20$21, e: TouchEventArgs)OnTouchLeave(self: ComboBox_21$22, e: TouchEventArgs)OnTouchLeave(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event 
             that occurs when a touch moves while inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchMove(self: Window_16$17, e: TouchEventArgs)OnTouchMove(self: Label_17$18, e: TouchEventArgs)OnTouchMove(self: TextBox_18$19, e: TouchEventArgs)OnTouchMove(self: Button_19$20, e: TouchEventArgs)OnTouchMove(self: CheckBox_20$21, e: TouchEventArgs)OnTouchMove(self: ComboBox_21$22, e: TouchEventArgs)OnTouchMove(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event 
             that occurs when a touch is released inside this element.
        
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        OnTouchUp(self: Window_16$17, e: TouchEventArgs)OnTouchUp(self: Label_17$18, e: TouchEventArgs)OnTouchUp(self: TextBox_18$19, e: TouchEventArgs)OnTouchUp(self: Button_19$20, e: TouchEventArgs)OnTouchUp(self: CheckBox_20$21, e: TouchEventArgs)OnTouchUp(self: ComboBox_21$22, e: TouchEventArgs)OnTouchUp(self: Separator_22$23, e: TouchEventArgs)
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is 
             modified.
        
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        OnVisualChildrenChanged(self: Window_16$17, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Label_17$18, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: TextBox_18$19, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Button_19$20, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: CheckBox_20$21, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: ComboBox_21$22, visualAdded: DependencyObject, visualRemoved: DependencyObject)OnVisualChildrenChanged(self: Separator_22$23, visualAdded: DependencyObject, visualRemoved: DependencyObject)
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. 
             Overrides 
             System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
        
            oldParent: The old parent element. May be null to indicate that the element did not have a 
             visual parent previously.
        
        OnVisualParentChanged(self: Window_16$17, oldParent: DependencyObject)OnVisualParentChanged(self: Label_17$18, oldParent: DependencyObject)OnVisualParentChanged(self: TextBox_18$19, oldParent: DependencyObject)OnVisualParentChanged(self: Button_19$20, oldParent: DependencyObject)OnVisualParentChanged(self: CheckBox_20$21, oldParent: DependencyObject)OnVisualParentChanged(self: ComboBox_21$22, oldParent: DependencyObject)OnVisualParentChanged(self: Separator_22$23, oldParent: DependencyObject)
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of 
             System.Windows.FrameworkElement. 
             System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement
             )  is invoked when a child element has invalidated a property that is marked in 
             metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        ParentLayoutInvalidated(self: Window_16$17, child: UIElement)ParentLayoutInvalidated(self: Label_17$18, child: UIElement)ParentLayoutInvalidated(self: TextBox_18$19, child: UIElement)ParentLayoutInvalidated(self: Button_19$20, child: UIElement)ParentLayoutInvalidated(self: CheckBox_20$21, child: UIElement)ParentLayoutInvalidated(self: ComboBox_21$22, child: UIElement)ParentLayoutInvalidated(self: Separator_22$23, child: UIElement)
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. 
             System.Windows.FrameworkElement updates the affected logical tree parent 
             pointers to keep in sync with this deletion.
        
        
            child: The element to remove.
        RemoveLogicalChild(self: Window_16$17, child: object)RemoveLogicalChild(self: Label_17$18, child: object)RemoveLogicalChild(self: TextBox_18$19, child: object)RemoveLogicalChild(self: Button_19$20, child: object)RemoveLogicalChild(self: CheckBox_20$21, child: object)RemoveLogicalChild(self: ComboBox_21$22, child: object)RemoveLogicalChild(self: Separator_22$23, child: object)
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        RemoveVisualChild(self: Window_16$17, child: Window_16$17)RemoveVisualChild(self: Label_17$18, child: Label_17$18)RemoveVisualChild(self: TextBox_18$19, child: TextBox_18$19)RemoveVisualChild(self: Button_19$20, child: Button_19$20)RemoveVisualChild(self: CheckBox_20$21, child: CheckBox_20$21)RemoveVisualChild(self: ComboBox_21$22, child: ComboBox_21$22)RemoveVisualChild(self: Separator_22$23, child: Separator_22$23)
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize 
             the value for the provided dependency property.
        
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; 
             otherwise, false.
        
        ShouldSerializeProperty(self: Window_16$17, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Label_17$18, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: TextBox_18$19, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Button_19$20, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: CheckBox_20$21, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: ComboBox_21$22, dp: DependencyProperty) -> bool
        ShouldSerializeProperty(self: Separator_22$23, dp: DependencyProperty) -> bool
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    DefiningGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    GeometryTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Windows.Media.Transform that is applied to this System.Windows.Shapes.Rectangle.

Get: GeometryTransform(self: Rectangle) -> Transform

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    RadiusX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-axis radius of the ellipse that is used to round the corners of the rectangle.

Get: RadiusX(self: Rectangle) -> float

Set: RadiusX(self: Rectangle) = value
"""

    RadiusY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-axis radius of the ellipse that is used to round the corners of the rectangle.

Get: RadiusY(self: Rectangle) -> float

Set: RadiusY(self: Rectangle) = value
"""

    RenderedGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Windows.Media.Geometry object that represents the final rendered shape.

Get: RenderedGeometry(self: Rectangle) -> Geometry

"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of visual child elements within this element.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


    RadiusXProperty = None
    RadiusYProperty = None


