import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {Component, Input} from '@angular/core';
import {
  Key,
  Type,
} from 'mesop/mesop/protos/ui_jspb_proto_pb/mesop/protos/ui_pb';
import {ButtonToggleType} from 'mesop/mesop/components/button_toggle/button_toggle_jspb_proto_pb/mesop/components/button_toggle/button_toggle_pb';
import {Channel} from '../../web/src/services/channel';

@Component({
  selector: 'mesop-button-toggle',
  templateUrl: 'button_toggle.ng.html',
  standalone: true,
  imports: [MatButtonToggleModule],
})
export class ButtonToggleComponent {
  @Input({required: true}) type!: Type;
  @Input() key!: Key;
  private _config!: ButtonToggleType;
  isChecked = false;

  constructor(private readonly channel: Channel) {}

  ngOnChanges() {
    this._config = ButtonToggleType.deserializeBinary(
      this.type.getValue() as unknown as Uint8Array,
    );
  }

  config(): ButtonToggleType {
    return this._config;
  }
}
